# -*- coding: utf-8 -*-
"""
..
    Copyright © 2017-2018 The University of New South Wales

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
    Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    Except as contained in this notice, the name or trademarks of a copyright holder

    shall not be used in advertising or otherwise to promote the sale, use or other
    dealings in this Software without prior written authorization of the copyright
    holder.

    UNSW is a trademark of The University of New South Wales.


libgs entrypoints
===================

:date: 2018-01-01
:author: Kjetil Wormnes



.. _libgs-db:

libgs-db
---------

libgs-db is a command-line tool to interact with any libgs-compatible database. It can connect to mysql databases, 
and to sqlite files, and in fact, to any other database permitted by SQLAlchemy.

For full reference::

    $ libgs-db --help

The most common use of libgs-db is to prune the databases to not get out of control. To do so, you should add a cron job to a script
that runs libgs-db to prune the database. It will look something like::

    libgs-db mysql+pymysql://uname:pwd@localhost/libgs[comms] --prune 1000 -d "sqlite:////backup/path/db.sqlite[comms]" --delete -f
    libgs-db mysql+pymysql://uname:pwd@localhost/libgs[passes] --prune 1000 -d "sqlite:////backup/path/db.sqlite[passes]" --delete -f
    libgs-db mysql+pymysql://uname:pwd@localhost/libgs[monitor] --prune 1000 -d "sqlite:////backup/path/db.sqlite[monitor]" --delete -f

This would prune the comms and passes tables to 1000 rows, backing up the excess rows into db.sqlite.

Another ommon use is to just quickly inspect the database to see the available tables. (This will work on non-libgs databases too)::

    $ libgs-db mysql+pymysql://uname:pwd@localhost/libgs
    No table specified. Do so by adding it in square brackets: mysql+pymysql://adfags:@dfags@localhost/adfags[table_name]
    I found the following tables in mysql+pymysql://adfags:@dfags@localhost/adfags:
    * passes ( 7374 rows )
        - _id                 INTEGER(11)
        - _tstamp             DECIMAL(20, 12)
        - key                 VARCHAR(1024)
        - value               TEXT
        - pass_id             VARCHAR(1024)
        - module              VARCHAR(1024)
    * monitor ( 224834 rows )
        - _id                 INTEGER(11)
        - _tstamp             DECIMAL(20, 12)
        - key                 VARCHAR(1024)
        - value               TEXT
        - pass_id             VARCHAR(1024)
        - alert               VARCHAR(1024)
    * comms ( 10008 rows )
        - _id                 INTEGER(11)
        - _tstamp             DECIMAL(20, 12)
        - nid                 VARCHAR(1024)
        - pass_id             VARCHAR(1024)
        - orig                VARCHAR(1024)
        - dest                VARCHAR(1024)
        - msg                 TEXT
        
Of course, you could do the same with a sqlite file. For example, to inspect the structure of the backup file created in above::

    $ libgs-db sqlite:////backup/path/db.sqlite

You could then inspect the contents of the specific tables, export to CSV, etc by specifying the table in square brackets. For example,
show the 3 most recent rows of the comms table::

    $ libgs-db mysql+pymysql://adfags:@dfags@localhost/adfags[comms] -l 3 -n
                            _tstamp    nid         pass_id orig dest                                                msg
    _id                                                                                                                
    19302 2018-10-29 04:10:56.150400  43014  20181029041407  Sat   GS  [0, 0, 182, 0, 17, 15, 167, 66, 186, 10, 18, 0...
    19301 2018-10-29 04:09:05.731200  43014  20181029041407  Sat   GS  [211, 1, 128, 0, 32, 59, 170, 84, 150, 165, 19...
    19300 2018-10-29 04:08:08.707200  43014  20181029041407  Sat   GS  [211, 1, 128, 0, 194, 97, 212, 76, 209, 74, 73...
    
See the ``--help`` reference for full details on the available arguments.     

libgs-restapi
--------------

    libgs-restapi is the command-line tool to start a libgs :mod:`.restapi`.

    For a full reference::

        $ libgs-restapi --help

    *Example*
    Create a restapi and connect it to the mysql database at localhost/libgs with username uname and password pwd, and use the
    binary path (where to store files that are too big for the database, see the disk_path in :class:`.database.Database`) as /libgs-db-bib.
    Bind publicly (0.0.0.0) on port 10001::

        $ libgs-restapi -a 0.0.0.0 -p 10001 --db mysql+pymysql://uname:pwd@localhost/libgs --db-bin-path /libgs-db-bin 

    *Example* Map RPC APIs.

    libgs-restapi has the ability to map an arbitrary XMLRPC api. See :mod:`.restapi` for details. In order to set it up using the libgs-restapi
    command-line tool use the -r parametr. For example::

        $ libgs-restapi -r rpc/gs http://localhost:10001 -r rpc/sch http://localhost:8000

    will create two additional api endpoints on ``/api/rpc/gs`` and ``/api/rpc/sch`` to which it will
    map the :class:`libgs.groundstation.GroundStation` and :class:`libgs.rpc.RPCSchedulerServer`  XMLRPC API interfaces respectively.

    Note that any XMLRPC interface can be mapped this way so long as it has registered introspection functions. 
    See SimpleXMLRPCServer. :meth:`~SimpleXMLRPCServer.SimpleXMLRPCServer.register_introspection_functions`. (you can of course also
    use :class:`libgs.rpc.RPCServer` as a drop-in replacement for SimpleXMLRPCServer anytime you make such an api)

    See the `--help` for detailed reference on avialable arguments   

libgs-emulate
--------------

    libgs-emulate is a console script thar can emulate certain hardware.

    Currently, it can emulate:

    * radio
    * rotctld

    For a full reference on available arguments run::
    
        $ libgs-emulate --help

    For emulator specific help run::

        $ libgs-emulate radio --help
        $ libgs-emulate rotctld --help


"""
from __future__ import print_function
import sys
import argparse
import pandas as pd
from utils import Defaults
import logging


def _print(*args, **kwargs):
    print(*args,file=sys.stderr, **kwargs)
    
def _fix_timestamp(when):
    if not isinstance(when, basestring):
        raise Exception("_fix_timestamp requires a string")
    return pd.to_datetime(when).strftime("%Y/%m/%d %H:%M:%S")
    
def _rev_timestamp(when):    
    if not isinstance(when, basestring):
        raise Exception("_rev_timestamp requires a string")
    return pd.to_datetime(when).strftime("%Y-%m-%dT%H:%M:%SZ")


def dbcontrol():
    """
    Entrypoint for libgs-db.

    See the :mod:`module help <.console_scripts>` for command-line usage details.

    """
    from libgs.database import CommsLog, MonitorDb, PassDb, Database, ID_LBL

    DEFAULTS = dict(
        limit = 1000
    )

    parser = argparse.ArgumentParser()

    parser.add_argument('database', help="An sqlalchemy compliant database target")
    parser.add_argument('-d', '--dump', type=str, help="Dump database to file or another db. In the case of another db\
                                specify it using sqlalchemy syntax, but with the table name added in square brackets.\
                                e.g. sqlite:///test.db[passes]")
    parser.add_argument('-o', '--overwrite-dump', action='store_true', help="If dump file/db exists, overwrite it (Default is to append)")
    parser.add_argument('--dbtype-dump', choices=['passes', 'comms', 'monitor', 'raw'], help='Specify the type of database to store to. Default is to infer from table name')
    parser.add_argument('-r', '--raw', action='store_true', help='Do not process data at all when reading from database. Binary/Date etc will be encoded')
    parser.add_argument('-R', '--raw-dump', action='store_true', help='Do not process data at all when saving data. Binary/Date etc will not be encoded. (Is only applied when saving to another database)')
    parser.add_argument('-n', '--newest-first', action="store_true", help="Get newest entries first. Default is to get oldest first")
    parser.add_argument('--no-sort-tstamp', action='store_true', help="Do not even query against timestamp column. Overrides -n")
    parser.add_argument('--delete', action='store_true', help="Delete from database after fetch")
    parser.add_argument('-f', '--force', action='store_true', help="Automatically answer yes to all questions")
    parser.add_argument('-l', '--limit', type=int,  help="Number of entries to fetch. Default={}".format(DEFAULTS['limit']))
    parser.add_argument('-m', '--map-column', nargs=2, action='append', help='Map column name in input to a different name in the output')
    parser.add_argument('--prune', type=int, help="The number of rows returned is such that <prune> number of rows are left. Cannot be used with --limit")


    args = parser.parse_args()


    def get_db_table(s):
        try:
            ssplit = s.split('[')
            db = ssplit[0]
            if len(ssplit) == 1:
                table = None
            elif len(ssplit) == 2:
                table = ssplit[1]
                assert table[-1] == ']'
                table = table[:-1]
            else:
                assert False
        except:
            raise Exception('Invalid syntax: ' + s)

        return db, table

    dbstr, table = get_db_table(args.database)

    try:
        db = Database(dbstr)
    except:
        print("Could not load database '{}'. Invalid syntax?".format(args.database))
        exit(1)

    if table is None:
        print("No table specified. Do so by adding it in square brackets: {}[table_name]".format(dbstr))
        print("I found the following tables in {}:".format(dbstr))

        for t in db._metadata.tables.keys():
            nrows = db.count_rows(t)
            print("  * {} ( {} rows )".format(t, nrows))
            for c in db._metadata.tables[t].columns:
                print("    - {:20s}{}".format(c.name, c.type))

        print("\n")

        exit(1)

    if args.prune is not None and args.limit is not None:
        print("--prune and --limit cannot be used together")
        exit(1)


    if args.limit is not None:
        limit = args.limit
    elif args.prune is not None:
        limit = db.count_rows(table) - args.prune
        if limit <= 0:
            print("No matches")
            exit(1)
    else:
        limit = DEFAULTS['limit']


    df = db.get_df(table, limit=limit, descending = args.newest_first if not args.no_sort_tstamp else None, raw=args.raw)

    # If the database had a primary key set it as index so we wont try to save it again later.
    if ID_LBL in df.columns:
        df = df.set_index(ID_LBL)
        has_primary_key = True
    else:
        has_primary_key = False

    if args.map_column:
        new_columns = df.columns.tolist()
        for k, v in args.map_column:
            if k not in new_columns:
                print("Warning: Column {} does not exist. Cannot map".format(k))
            else:
                #print("Mapped column '{}' to '{}'".format(k, v))
                new_columns[new_columns.index(k)] = v

        df.columns = new_columns

    if args.dump:
        try:
            out_dbstr, out_table = get_db_table(args.dump)
            out_db = Database(db = out_dbstr, binary_fmt='b64')
        except Exception as e:
            # print("{}: {}".format(e.__class__.__name__, e))
            out_dbstr = None
            out_db = None
            out_table  = None


        if out_db is None:
            file_format = args.dump.split('.')[-1]
            valid_dump_formats = ['csv', 'json', 'p', 'pickle']
            if file_format not in valid_dump_formats:
                print("Invalid dump format. Valid formats are {}".format(valid_dump_formats))
                exit(1)

            # TODO: Implement append/overwrite for file output
            if args.overwrite_dump:
                print("-a and -o have not been implemented for file output yet")
                exit(1)

            if file_format == 'csv':
                df.to_csv(args.dump)
            elif file_format == 'json':
                df.to_json(args.dump)
            elif file_format == 'p' or file_format == 'pickle':
                df.to_pickle(args.dump)
            else:
                print('Invalid dump format {}'.format(file_format))
                exit(1)

        else:
            if out_table is None:
                print("Failed to parse table name from dqlalchemy string '{}'".format(args.dump))
                exit(1)

            # This just initialises the database tables if not done already
            if args.dbtype_dump is None:
                dbtype_dump = out_table
            else:
                dbtype_dump = args.dbtype_dump

            if args.overwrite_dump:
                try:
                    out_db._metadata.tables[out_table].drop()
                except Exception as e:
                    print("Failed to drop table. {}: {}".format(e.__class__.__name__, e))

                if_exists = 'append'

            # Create the tables properly (thats why we use if_exists=append in the overwrite case
            if dbtype_dump == 'passes':
                out_db = PassDb(out_dbstr)
            elif dbtype_dump == 'monitor':
                out_db = MonitorDb(out_dbstr)
            elif dbtype_dump == 'comms':
                out_db = CommsLog(out_dbstr)

            #
            # Do not use the out_db.put_df call since we do not want to save the timestamps
            #

            # Encode binary data
            if not args.raw_dump:
                df = df.applymap(out_db._encode)


            df.to_sql(table, out_db._eng, if_exists='append', index=False)


    print(df.to_string())

    if args.delete:
        if not has_primary_key:
            print("ERROR: Cannot drop items from database that does not have a primary key")
        else:
            proceed = False
            if args.force:
                proceed = True
            else:
                inp = raw_input("This will delete all the found entries from the original database. Continue? y/[n]")
                if inp == 'y':
                    proceed = True

            if proceed:
                t = db._metadata.tables[table]
                for k,r in df.iterrows():
                    print('Dropping _id={}'.format(k))
                    db._eng.execute(t.delete().where(t.columns[ID_LBL] == k))






   
def restapi():
    """
    Entry point for the libgs REST API.

    See the :mod:`module help <.console_scripts>` for command-line usage details.
     
    """
    from libgs.database import CommsLog, MonitorDb, PassDb
    from libgs.restapi  import RESTAPI
    import time
    
    allowed_formats = ['html','json', 'csv']
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-a', '--addr', 
                        default=Defaults.API_ADDR, type=str, 
                        help='Address to bind REST API to. Default = {}'.format(Defaults.API_ADDR))
    parser.add_argument('-p', '--port', 
                        default=Defaults.API_PORT, type=int, 
                        help='Port to bind REST API to. Default = {}'.format(Defaults.API_PORT))
    parser.add_argument('-f', '--format',
                        default='json', type=str,
                        help='Format to display results in by preference. Must be one of {}'.format(allowed_formats))
    parser.add_argument('-d', '--debug',
                        action='store_true', help='Enable debug output. ')
    parser.add_argument("--allowed", nargs='*', help="List of URI patterns to permit. If not supplied all patterns are permitted")
    parser.add_argument('--db', type=str, default=Defaults.DB,
                        help='Communications log database engine specification, for example sqlite:///test.db, or mysql+pymysql://<uname>:<pwd>@<host>/<db>, or... Default is %s'%(Defaults.DB))
    parser.add_argument("--db-bin-path", type=str, default=Defaults.DB_BIN_PATH, help="Files larger than a threshold are stored in file system. Specify where. Default is '{}'".format(Defaults.DB_BIN_PATH))
    parser.add_argument('-v', '--verbose', action="count", 
                        help='Increase verbosity level displayed on the\
                        console. Default is ERRORs only')
    parser.add_argument("-r", "--rpcapi", nargs=2, metavar = ('uri', 'addr'), action="append", help="Add RPCAPI")
                        
                        
    args = parser.parse_args()


    #
    # Set up consoloe logging as specificed
    #    
    if args.verbose == 0 or args.verbose is None:
        cons_loglevel = logging.ERROR
    elif args.verbose == 1:
        cons_loglevel = logging.INFO
    elif args.verbose == 2:
        cons_loglevel = logging.DEBUG
    else:
        raise Exception("Invalid verbosity level")
    
    
    log = logging.getLogger('libgs-log')
    log.setLevel(cons_loglevel)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(Defaults.LOG_FORMAT)
    ch.setFormatter(formatter)
    log.addHandler(ch)
    
    
    if args.format not in allowed_formats:
        raise Exception('Format must be one of %s'%allowed_formats)
    
    
    commdb = CommsLog(db=args.db, disk_path=args.db_bin_path)
    mondb  = MonitorDb(db=args.db, disk_path=args.db_bin_path)
    passdb = PassDb(db=args.db, disk_path=args.db_bin_path)
    
    if args.rpcapi is not None:
        rpcapi = dict(args.rpcapi)
    else:
        rpcapi = None
    
    api = RESTAPI(\
             commslog = commdb,
             monlog   = mondb,
             passdb   = passdb,
             host     = args.addr,
             port     = args.port,
             default_format=args.format,
             rpcapi   = rpcapi,
             allowed  = args.allowed) 


    api.start()    
        
    print('CTRL-C to exit')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            log.info("KeyboardInterrupt received. Cleaning up.")
            api.stop()
            break



         
def emulate():
    """
    Entrypoint for libgs-emulate.

    See the :mod:`module help <.console_scripts>` for command-line usage details.
         
    """
    from emulators import Radio
    import time
    
    DEFAULTS = {
        'freq': 449e6,
        'samp-rate': 74e3,
        'range-rate': 1000,
        'rpcvar-freq': 'freq',
        'rpcvar-samp-rate': 'samp_rate',
        'rpcvar-range-rate': 'rangeRate'}
    
    parser = argparse.ArgumentParser()
    emulators = ['radio', 'rotctld']
    
    subparsers = parser.add_subparsers(help='sub-command help', dest='emulator')
    parser_radio = subparsers.add_parser('radio', help='help on radio emulator')
    parser_radio.add_argument('--rpc-port', '-r', type=int, default=8051, help="Port to bind RPC to")
    parser_radio.add_argument('--iq-port', '-i', type=int, default=5551, help="ZMQ port to publish IQ samples on")
    parser_radio.add_argument('-f', '--freq', type=float, default=DEFAULTS['freq'], help="Centre frequency to use and report. The XMLRPC function are get_freq, and set_freq. Default = {}".format(DEFAULTS['freq']))
    parser_radio.add_argument('-s', '--samp-rate', type=float, default=DEFAULTS['samp-rate'], help="Sample rate to use and report. The XMLRPC functions are get_samp_rate and set_samp_rate. Default = {}".format(DEFAULTS['samp-rate']))
    parser_radio.add_argument('--range-rate', type=float, default=DEFAULTS['range-rate'], help="Range rate to report. The XMLRPC function are get_range_rate and set_range_rate. Default = {}".format(DEFAULTS['range-rate']))
    parser_radio.add_argument('--rpcvar-freq', default=DEFAULTS['rpcvar-freq'], help="The RPC variable to use for frequency. Default = {}".format(DEFAULTS['rpcvar-freq']))
    parser_radio.add_argument('--rpcvar-samp-rate', default=DEFAULTS['rpcvar-samp-rate'], help="The RPC variable to use for sample rate. Default = {}".format(DEFAULTS["rpcvar-samp-rate"]))
    parser_radio.add_argument('--rpcvar-range-rate', default=DEFAULTS['rpcvar-range-rate'], help="The RPC variable to use for range rate. Default = {}".format(DEFAULTS["rpcvar-range-rate"]))

    parser_rotctld = subparsers.add_parser('rotctld', help="Help on RotCtld emulator TODO")
    parser_rotctld.add_argument('--todo')

    args = parser.parse_args()    

    if args.emulator == "radio":
        radio = Radio(\
                    port=args.rpc_port, 
                    ifvars = {args.rpcvar_freq:args.freq, args.rpcvar_samp_rate:args.samp_rate, args.rpcvar_range_rate:args.range_rate},
                    iqport = args.iq_port)
                    
        print("Starting radio emulator. Serving XMLRPC requests on http://localhost:{} and IQ data on http://localhost:{}".format(args.rpc_port, args.iq_port))
        radio.start()
        
        while True:
            
            try:
                time.sleep(1)
            except:
                break
        
        print("Stopped radio emulator")
        radio.stop()
        
                    
        

