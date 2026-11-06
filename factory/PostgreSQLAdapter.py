from factory.DBAdapter import DBAdapter
import psycopg2

class PostgreSQLAdapter(DBAdapter):
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        conn = psycopg2.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            dbname=self.config['database'],
            port=self.config.get('port', 5432)
        )
        conn.autocommit = True
        return conn

    def execute(self, sql, params=None):
        sql_format = sql.replace('?', '%s')
        cursor = self.get_connection().cursor()
        if params:
            cursor.execute(sql_format, params)
        else:
            cursor.execute(sql_format)
        self.commit()

    def execute_query(self, sql, params=None):
        sql_format = sql.replace('?', '%s')
        cursor = self.get_connection().cursor()
        if params:
            cursor.execute(sql_format, params)
        else:
            cursor.execute(sql_format)
        return cursor

    def getCursor(self):
        return self.get_connection().cursor()

    def close(self):
        self.get_connection().close()

    def commit(self):
        self.get_connection().commit()