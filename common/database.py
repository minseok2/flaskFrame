
from flask import current_app
from common.utils import *

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]

class Database(metaclass=Singleton):

    def __init__(self):
        self.db_type = current_app.config['DB_TYPE']
        self.db_path = current_app.config['DB_PATH']

        host, port, id, pw, db_name = get_db_info(self.db_path)

        if self.db_type == 1:
            import pymysql
            self.db = pymysql.connect(
                            host=host,
                            port=port,
                            user=id,
                            password=pw,
                            database=db_name,
                            autocommit=True
                        )
        elif self.db_type == 2:
            import psycopg2 as pg2
            self.db = pg2.connect(
                            host=host,
                            port=port,
                            user=id,
                            password=pw,
                            database=db_name
                        )
        elif self.db_type == 3:
            import cx_Oracle
            db_info = '{}/{}@{}:{}/{}'.format(id, pw, host, port, db_name)
            self.db = cx_Oracle.connect(db_info)
        self.cursor = self.db.cursor()

    def execute(self, query, args):
        self.cursor.execute(query, args)

    def executeMany(self, query, args):
        self.cursor.executemany(query, args)

    def executeOne(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

    def __del__(self):
        del self.cursor
        del self.db
