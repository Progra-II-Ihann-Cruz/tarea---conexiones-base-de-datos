from factory.DBAdapter import DBAdapter
import pymysql.cursors

class MySqlAdapter(DBAdapter):
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        return pymysql.connect(
            host=self.config['host'],
            user=self.config['user'],
            passwd=self.config['password'],
            db=self.config['database'],
            charset='utf8mb4',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )

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