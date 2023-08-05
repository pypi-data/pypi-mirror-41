import os
import sys
import sqlite3
import csv
import locale
import random
import string
import signal
import logging
import platform
from contextlib import contextmanager
from itertools import groupby

import coloredlogs
import psutil
import pandas as pd
from sas7bdat import SAS7BDAT
from graphviz import Digraph
from more_itertools import spy, chunked
from pathos.multiprocessing import ProcessingPool as Pool
from progressbar import progressbar
if platform.system() == "Darwin":
    from shutil import copyfile


_locale = 'English_United States.1252' if os.name == 'nt' else 'en_US.UTF-8'

_CONFIG = {
    'ws': '',
    'max_workers': psutil.cpu_count(logical=False),
    'locale': _locale,
    'msg': True,
}

_filename, _ = os.path.splitext(os.path.basename(sys.argv[0]))
_DBNAME = _filename + '.db'
_GRAPH_NAME = _filename + '.gv'
_JOBS = {}
# folder name (in workspace) for temporary databases for parallel work
_TEMP = "_temp"

coloredlogs.DEFAULT_FIELD_STYLES['levelname']['color'] = 'cyan'
coloredlogs.install(
    fmt='%(asctime)s %(levelname)s %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


# TODO: better error messages
class FeebeeError(Exception):
    pass


class NoRowToInsert(FeebeeError):
    pass


class InvalidGroup(FeebeeError):
    pass


class UnknownConfig(FeebeeError):
    pass


@contextmanager
def _connect(dbfile):
    conn = _Connection(dbfile)
    try:
        yield conn
    finally:
        # Trying to make closing atomic to handle multiple ctrl-cs
        # Imagine the first ctrl-c have the process enter the 'finally block'
        # and the second ctrl-c interrupts the block in the middle
        # so that the database is corrupted
        with _delayed_keyboard_interrupts():
            # should I close the cursor?
            conn._cursor.close()
            conn._conn.commit()
            conn._conn.close()


@contextmanager
def _delayed_keyboard_interrupts():
    signal_received = []

    def handler(sig, frame):
        nonlocal signal_received
        signal_received = (sig, frame)
        logger.debug('SIGINT received. Delaying KeyboardInterrupt.')
    old_handler = signal.signal(signal.SIGINT, handler)

    try:
        yield
    finally:
        signal.signal(signal.SIGINT, old_handler)
        if signal_received:
            old_handler(*signal_received)


class _Connection:
    def __init__(self, dbfile):
        if not _CONFIG['ws']:
            _CONFIG['ws'] = os.getcwd()
        dbfile = os.path.join(_CONFIG['ws'], dbfile)
        locale.setlocale(locale.LC_ALL, _CONFIG['locale'])
        logger.propagate = _CONFIG['msg'] 

        self._conn = sqlite3.connect(dbfile)
        self._conn.row_factory = _dict_factory
        self._cursor = self._conn.cursor()
        # DO NOT re_CONFIGure pragmas. Defaults are defaults for a reason.
        # You could make it faster but with a cost. It could corrupt the disk image of the database.

    def fetch(self, query, where=None, by=None):
        if by and isinstance(by, list) and by != ['*'] and all(isinstance(c, str) for c in by):
            query += " order by " + ','.join(by)
        rows = self._conn.cursor().execute(query)
        if where:
            rows = (r for r in rows if where(r))
        if by:
            if isinstance(by, list):
                rows1 = (list(rs) for _, rs in groupby(rows, _build_keyfn(by)))
            elif isinstance(by, int):
                rows1 = chunked(rows, by)
            else:
                raise InvalidGroup(by)
            yield from rows1
        else:
            yield from rows

    def insert(self, rs, name):
        r0, rs = spy(rs)
        if r0 == []:
            raise NoRowToInsert(name)

        cols = list(r0[0])
        self._cursor.execute(_create_statement(name, cols))
        istmt = _insert_statement(name, r0[0])
        self._cursor.executemany(istmt, rs)

    def load(self, filename, name, delimiter=None, quotechar='"',
             encoding='utf-8', fn=None):
        if isinstance(filename, str):
            _, ext = os.path.splitext(filename)
            if ext.lower() == '.xlsx' or ext.lower() == ".xls":
                seq = _read_excel(filename)
            elif ext.lower() == '.sas7bdat':
                seq = _read_sas(filename)
            elif ext.lower() == ".dta":
                seq = _read_stata(filename)
            else:
                # default delimiter is ","
                delimiter = delimiter or ("\t" if ext.lower() == ".tsv" else ",")
                seq = _read_csv(filename, delimiter=delimiter, quotechar=quotechar,
                                encoding=encoding)
        else:
            # iterator, since you can pass an iterator
            # functions of 'load' should be limited
            seq = filename

        if fn:
            seq = _flatten(fn(rs) for rs in seq)
        self.insert(progressbar(seq), name)

    def get_tables(self):
        query = self._cursor.execute("select * from sqlite_master where type='table'")
        return [row['name'] for row in query]

    def drop(self, tables):
        tables = _listify(tables)
        for table in tables:
            self._cursor.execute(f'drop table if exists {table}')

    def join(self, tinfos, name):
        tname0, _, mcols0 = tinfos[0]
        join_clauses = []
        for i, (tname1, _, mcols1) in enumerate(tinfos[1:], 1):
            eqs = []
            for c0, c1 in zip(_listify(mcols0), _listify(mcols1)):
                if c1:
                    # allows expression such as 'col + 4' for 'c1', for example.
                    # somewhat sneaky though
                    eqs.append(f't0.{c0} = t{i}.{c1}')
            join_clauses.append(f"left join {tname1} as t{i} on {' and '.join(eqs)}")
        jcs = ' '.join(join_clauses)

        allcols = []
        for i, (_, cols, _) in enumerate(tinfos):
            for c in _listify(cols):
                if c == '*':
                    allcols += [f't{i}.{c1}' for c1 in self._cols(f'select * from {tinfos[i][0]}')]
                else:
                    allcols.append(f't{i}.{c}')

        # create indices
        ind_tnames = []
        for tname, _, mcols in tinfos:
            mcols1 = [c for c in _listify(mcols) if c]
            ind_tname = tname + _random_string(10)
            # allows expression such as 'col + 4' for indexing, for example.
            # https://www.sqlite.org/expridx.html
            self._cursor.execute(f"create index {ind_tname} on {tname}({', '.join(mcols1)})")

        query = f"create table {name} as select {', '.join(allcols)} from {tname0} as t0 {jcs}"
        self._cursor.execute(query)
        # drop indices, not so necessary
        for ind_tname in ind_tnames:
            self._cursor.execute(f"drop index {ind_tname}")

    def _cols(self, query):
        return [c[0] for c in self._cursor.execute(query).description]

    def _size(self, table):
        self._cursor.execute(f"select count(*) as c from {table}")
        return self._cursor.fetchone()['c']


def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def _flatten(seq):
    for x in seq:
        if isinstance(x, dict):
            yield x
        else:
            yield from x


def _applyfn(fn, seq, arg):
    if arg:
        yield from _flatten(fn(rs, arg) for rs in seq)
    else:
        yield from _flatten(fn(rs) for rs in seq)


def _execute(c, job):
    cmd = job['cmd']
    if cmd == 'load':
        c.load(job['file'], job['output'], delimiter=job['delimiter'],
               quotechar=job['quotechar'], encoding=job['encoding'], fn=job['fn'])
    elif cmd == 'map':
        if job['parallel']:
            max_workers = int(job['parallel']) if job['parallel'] >= 2 else _CONFIG['max_workers']
            max_workers = min(max_workers, psutil.cpu_count())
            tsize = c._size(job['inputs'][0])
        if job['parallel'] and (job['by'].strip() != '*' if job['by'] else True) and\
            max_workers > 1 and tsize >= max_workers:
            if platform.system() == 'Darwin':
                _exec_parallel_map_darwin(c, job, max_workers, tsize)
            else:
                _exec_parallel_map_non_darwin(c, job, max_workers, tsize)
        else:
            seq = c.fetch(f"select * from {job['inputs'][0]}", job['where'], _listify(job['by']))
            seq1 = _applyfn(job['fn'], seq, job['arg'])
            c.insert(progressbar(seq1), job['output'])

    elif cmd == 'join':
        c.join(job['args'], job['output'])

    elif cmd == 'union':
        def gen():
            for inp in job['inputs']:
                for r in c.fetch(f"select * from {inp}"):
                    yield r
        c.insert(gen(), job['output'])


# sqlite3 in osx can't handle multiple connections properly.
def _exec_parallel_map_darwin(c, job, max_workers, tsize):
    itable = job['inputs'][0]
    tdir = os.path.join(_CONFIG['ws'], _TEMP)
    if not os.path.exists(tdir):
        os.makedirs(tdir)
    dbfiles = [os.path.join(_TEMP, _random_string(10)) for _ in range(max_workers)]

    tcon = 'con' + _random_string(9)
    ttable = "tbl" + _random_string(9)
    # Rather expensive
    breaks = [int(i * tsize / max_workers) for i in range(1, max_workers)]
    bys = _listify(job['by']) if job['by'] else None
    exe = Pool(len(dbfiles))

    def _proc(dbfile, cut):
        query = f"select * from {ttable} where _ROWID_ > {cut[0]} and _ROWID_ <= {cut[1]}"
        with _connect(dbfile) as c1:
            seq = _applyfn(job['fn'], c1.fetch(query, where=job['where'], by=bys), job['arg'])
            try:
                c1.insert(progressbar(seq), job['output'])
            except NoRowToInsert:
                pass

    def _collect_tables(dbfiles):
        succeeded_dbfiles = []
        for dbfile in dbfiles:
            with _connect(dbfile) as c1:
                if job['output'] in c1.get_tables():
                    succeeded_dbfiles.append(dbfile)

        if succeeded_dbfiles == []:
            raise NoRowToInsert

        with _connect(succeeded_dbfiles[0]) as c1:
            ocols = c1._cols(f"select * from {job['output']}")
        c._cursor.execute(_create_statement(job['output'], ocols))

        # collect tables from dbfiles
        for dbfile in succeeded_dbfiles:
            c._cursor.execute(f"attach database '{dbfile}' as {tcon}")
            c._cursor.execute(f"insert into {job['output']} select * from {tcon}.{job['output']}")
            c._conn.commit()
            c._cursor.execute(f"detach database {tcon}")

    def _delete_dbfiles(dbfiles):
        with _delayed_keyboard_interrupts():
            for dbfile in dbfiles:
                if os.path.exists(dbfile):
                    os.remove(dbfile)

    # condition for parallel work by group
    if bys:
        try:
            c._cursor.execute(f"attach database '{dbfiles[0]}' as {tcon}")
            c._cursor.execute(f"""
            create table {tcon}.{ttable} as select * from {itable} order by {','.join(bys)}
            """)
            c._conn.commit()
            c._cursor.execute(f"detach database {tcon}")

            with _connect(dbfiles[0]) as c1:
                def nth_gcols(n):
                    c1._cursor.execute(f"select * from {ttable} where _ROWID_ == {n} limit 1")
                    r = c1._cursor.fetchone()
                    return [r[c] for c in bys]

                def where1(br):
                    return ' and '.join(f"{c} = {repr(v)}" for c, v in zip(bys, nth_gcols(br)))

                def build_wheres(breaks):
                    return ' or '.join(where1(br) for br in breaks)
    
                newbreaks = [list(r.values())[0] for r in c1._cursor.execute(f"""
                select _ROWID_ from {ttable}
                where {build_wheres(breaks)} group by {','.join(bys)} having MAX(_ROWID_)
                """)] + [tsize]
            for dbfile in dbfiles[1:]:
                copyfile(dbfiles[0], dbfile)

            exe.map(_proc, dbfiles, zip([0] + newbreaks, newbreaks))
            _collect_tables(dbfiles)
        finally:
            _delete_dbfiles(dbfiles)

    # non group parallel work
    else:
        try:
            c._cursor.execute(f"attach database '{dbfiles[0]}' as {tcon}")
            c._cursor.execute(f"create table {tcon}.{ttable} as select * from {itable}")
            c._conn.commit()
            c._cursor.execute(f"detach database {tcon}")
            for dbfile in dbfiles[1:]:
                copyfile(dbfiles[0], dbfile)

            exe.map(_proc, dbfiles, zip([0] + breaks, breaks + [tsize]))
            _collect_tables(dbfiles)
        finally:
            _delete_dbfiles(dbfiles)


def _exec_parallel_map_non_darwin(c, job, max_workers, tsize):
    itable = job['inputs'][0]
    tdir = os.path.join(_CONFIG['ws'], _TEMP)
    if not os.path.exists(tdir):
        os.makedirs(tdir)
    dbfiles = [os.path.join(_TEMP, _random_string(10)) for _ in range(max_workers - 1)]

    tcon = 'con' + _random_string(9)
    ttable = "tbl" + _random_string(9)
    # Rather expensive
    breaks = [int(i * tsize / max_workers) for i in range(1, max_workers)]
    bys = _listify(job['by']) if job['by'] else None
    exe = Pool(len(dbfiles) + 1)

    def _split_table(source_table, breaks, dbfiles):
        for (a, b), dbfile in zip(zip(breaks, breaks[1:] + [tsize]), dbfiles):
            c._cursor.execute(f"attach database '{dbfile}' as {tcon}")
            c._cursor.execute(f"""
            create table {tcon}.{source_table} as select * from {source_table}
            where _ROWID_ > {a} and _ROWID_ <= {b}
            """)
            c._conn.commit()
            c._cursor.execute(f"detach database {tcon}")

    def _proc(dbfile):
        source = ttable if bys else itable
        if isinstance(dbfile, int):
            query = f"select * from {source} where _ROWID_ <= {dbfile}"
            dbfile = _DBNAME
        else:
            query = f"select * from {source}"

        with _connect(dbfile) as c1:
            seq = _applyfn(job['fn'], c1.fetch(query, where=job['where'], by=bys),
                            job['arg'])
            try:
                c1.insert(progressbar(seq), job['output'])
            except NoRowToInsert:
                pass

    def _collect_tables(dbfiles):
        succeeded_dbfiles = []
        for dbfile in dbfiles:
            with _connect(dbfile) as c1:
                if job['output'] in c1.get_tables():
                    succeeded_dbfiles.append(dbfile)

        if succeeded_dbfiles == [] and (job['output'] not in c.get_tables()):
            raise NoRowToInsert

        if job['output'] not in c.get_tables():
            with _connect(succeeded_dbfiles[0]) as c1:
                ocols = c1._cols(f"select * from {job['output']}")
            c._cursor.execute(_create_statement(job['output'], ocols))
        # collect tables from dbfiles
        for dbfile in succeeded_dbfiles:
            c._cursor.execute(f"attach database '{dbfile}' as {tcon}")
            c._cursor.execute(f"""
            insert into {job['output']} select * from {tcon}.{job['output']}
            """)
            c._conn.commit()
            c._cursor.execute(f"detach database {tcon}")

    def _delete_dbfiles(dbfiles):
        with _delayed_keyboard_interrupts():
            for dbfile in dbfiles:
                if os.path.exists(dbfile):
                    os.remove(dbfile)
            c.drop(ttable)

    # condition for parallel work by group
    if bys:
        try:
            c._cursor.execute(f"""
            create table {ttable} as select * from {itable} order by {','.join(bys)}
            """)

            def nth_gcols(n):
                c._cursor.execute(f"select * from {ttable} where _ROWID_ == {n} limit 1")
                r = c._cursor.fetchone()
                return [r[c] for c in bys]

            def where1(br):
                return ' and '.join(f"{c} = {repr(v)}" for c, v in zip(bys, nth_gcols(br)))

            def build_wheres(breaks):
                return ' or '.join(where1(br) for br in breaks)

            # don't use r['_rowid_'] here
            newbreaks = [list(r.values())[0] for r in c._cursor.execute(f"""
            select _ROWID_ from {ttable}
            where {build_wheres(breaks)} group by {','.join(bys)} having MAX(_ROWID_)
            """)] + [tsize]

            _split_table(ttable, newbreaks, dbfiles)
            exe.map(_proc, [newbreaks[0]] + dbfiles)
            _collect_tables(dbfiles)
        finally:
            _delete_dbfiles(dbfiles)

    # non group parallel work
    else:
        try:
            _split_table(itable, breaks, dbfiles)
            exe.map(_proc, [breaks[0]] + dbfiles)
            _collect_tables(dbfiles)
        finally:
            _delete_dbfiles(dbfiles)


def load(file=None, fn=None, delimiter=None, quotechar='"', encoding='utf-8'):
    return {'cmd': 'load',
            'file': file,
            'fn': fn,
            'delimiter': delimiter,
            'quotechar': quotechar,
            'encoding': encoding,
            'inputs': []}


def map(fn=None, data=None, where=None, by=None, arg=None, parallel=False):
    return {
        'cmd': 'map',
        'fn': fn,
        'inputs': [data],
        'where': where,
        'by': by,
        'arg': arg,
        'parallel': parallel
    }


def join(*args):
    inputs = [arg[0] for arg in args]
    return {
        'cmd': 'join',
        'inputs': inputs,
        'args': args
    }


def union(inputs):
    return {
        'cmd': 'union',
        'inputs': _listify(inputs)
    }


def register(**kwargs):
    for k, _ in kwargs.items():
        if _JOBS.get(k, False):
            raise ValueError(f"Table duplication: {k}")
    _JOBS.update(kwargs)


def run(**kwargs):
    global _CONFIG
    try:
        default_configs = {k: v for k, v in _CONFIG.items()}
        for k, v in kwargs.items():
            if k not in _CONFIG:
                raise UnknownConfig(k)
            _CONFIG[k] = v
        return _run()
    finally:
        _CONFIG = default_configs


def _run():
    def append_output(kwargs):
        for k, v in kwargs.items():
            v['output'] = k
        return [v for _, v in kwargs.items()]

    def find_required_tables(jobs):
        tables = set()
        for job in jobs:
            for table in job['inputs']:
                tables.add(table)
            tables.add(job['output'])
        return tables

    # depth first search
    def dfs(graph, path, paths=[]):
        datum = path[-1]
        if datum in graph:
            for val in graph[datum]:
                new_path = path + [val]
                paths = dfs(graph, new_path, paths)
        else:
            paths += [path]
        return paths

    # graph: {input: [out1, out2, ...]}
    def build_graph(jobs):
        graph = {}
        for job in jobs:
            for ip in job['inputs']:
                if graph.get(ip):
                    graph[ip].add(job['output'])
                else:
                    graph[ip] = {job['output']}
        for x in graph:
            graph[x] = list(graph[x])
        return graph

    def render_graph(graph, jobs):
        dot = Digraph()
        for k, v in graph.items():
            dot.node(k, k)
            if k != v:
                for v1 in v:
                    dot.edge(k, v1)
        for job in jobs:
            if job['cmd'] == 'load':
                dot.node(job['output'], job['output'])
        dot.render(_GRAPH_NAME)

    jobs = append_output(_JOBS)
    required_tables = find_required_tables(jobs)
    with _connect(_DBNAME) as c:
        def delete_after(missing_table, paths):
            for path in paths:
                if missing_table in path:
                    for x in path[path.index(missing_table):]:
                        c.drop(x)

        def get_missing_tables():
            existing_tables = c.get_tables()
            return [table for table in required_tables
                    if table not in existing_tables]

        def find_jobs_to_do(jobs):
            missing_tables = get_missing_tables()
            result = []
            for job in jobs:
                for table in job['inputs'] + [job['output']]:
                    if table in missing_tables:
                        result.append(job)
                        break
            return result

        def is_doable(job):
            missing_tables = get_missing_tables()
            return all(table not in missing_tables for table in job['inputs']) \
                and job['output'] in missing_tables

        graph = build_graph(jobs)
        try:
            render_graph(graph, jobs)
        except Exception:
            pass

        starting_points = [job['output'] for job in jobs if job['cmd'] == 'load']
        paths = []
        for sp in starting_points:
            paths += dfs(graph, [sp], [])

        for mt in get_missing_tables():
            delete_after(mt, paths)

        jobs_to_do = find_jobs_to_do(jobs)
        initial_jobs_to_do = list(jobs_to_do)
        logger.info(f'To Create: {[j["output"] for j in jobs_to_do]}')
        while jobs_to_do:
            cnt = 0
            for i, job in enumerate(jobs_to_do):
                if is_doable(job):
                    try:
                        logger.info(f"processing {job['cmd']}: {job['output']}")
                        _execute(c, job)
                    except Exception as e:
                        logger.error(f"Failed: {job['output']}")
                        logger.error(f"{type(e).__name__}: {e}")
                        try:
                            c.drop(job['output'])
                        except Exception:
                            pass

                        logger.warning(f"Unfinished: {[job['output'] for job in jobs_to_do]}")
                        return (initial_jobs_to_do, jobs_to_do)
                    del jobs_to_do[i]
                    cnt += 1
            # No jobs can be done anymore
            if cnt == 0:
                for j in jobs_to_do:
                    logger.warning(f'Unfinished: {j["output"]}')
                    for t in j['inputs']:
                        if t not in c.get_tables():
                            logger.warning(f'Table not found: {t}')
                return (initial_jobs_to_do, jobs_to_do)
        # All jobs done well
        return (initial_jobs_to_do, jobs_to_do)


def _random_string(nchars):
    "Generates a random string of lengh 'n' with alphabets and digits. "
    chars = string.ascii_letters + string.digits
    return ''.join(random.SystemRandom().choice(chars)
                   for _ in range(nchars))


def _listify(x):
    if isinstance(x, str):
        return [x1.strip() for x1 in x.split(',')]
    if isinstance(x, tuple):
        return list(x)
    return x


def _build_keyfn(key):
    colnames = _listify(key)
    # special case
    if colnames == ['*']:
        return lambda r: 1

    if len(colnames) == 1:
        col = colnames[0]
        return lambda r: r[col]
    return lambda r: [r[colname] for colname in colnames]


# primary keys are too much for non-experts
def _create_statement(name, colnames):
    """create table if not exists foo (...)

    Note:
        Every type is numeric.
        Table name and column names are all lowercased
    """
    # every col is numeric, this may not be so elegant but simple to handle.
    # If you want to change this, Think again
    schema = ', '.join([col + ' ' + 'numeric' for col in colnames])
    return "create table if not exists %s (%s)" % (name, schema)


# column can contain spaces. So you must strip them all
def _insert_statement(name, d):
    "insert into foo values (:a, :b, :c, ...)"
    keycols = ', '.join(":" + c.strip() for c in d)
    return "insert into %s values (%s)" % (name, keycols)


def _read_csv(filename, delimiter=',', quotechar='"', encoding='utf-8'):
    with open(os.path.join(_CONFIG['ws'], filename), encoding=encoding) as f:
        header = [c.strip() for c in f.readline().split(delimiter)]
        yield from csv.DictReader(f, fieldnames=header,
                                  delimiter=delimiter, quotechar=quotechar)


def _read_sas(filename):
    filename = os.path.join(_CONFIG['ws'], filename)
    with SAS7BDAT(filename) as f:
        reader = f.readlines()
        header = [c.strip() for c in next(reader)]
        for line in reader:
            yield {k: v for k, v in zip(header, line)}


def _read_df(df):
    cols = df.columns
    header = [c.strip() for c in df.columns]
    for _, r in df.iterrows():
        yield {k: v for k, v in zip(header, ((str(r[c]) for c in cols)))}


# this could be more complex but should it be?
def _read_excel(filename):
    filename = os.path.join(_CONFIG['ws'], filename)
    # it's OK. Excel files are small
    df = pd.read_excel(filename)
    yield from _read_df(df)


# raises a deprecation warning
def _read_stata(filename):
    filename = os.path.join(_CONFIG['ws'], filename)
    chunk = 10_000
    for xs in pd.read_stata(filename, chunksize=chunk):
        yield from _read_df(xs)
