from factory.DBAdapter import DBAdapter
import pyodbc

class MSQLSvrAdapter(DBAdapter):

    def __init__(self, config):
        self.config = config

    def get_connection(self):
        return pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" +
                              f"Server={self.config['host']};" +
                              f"Database={self.config['database']};" +
                              f"Uid={self.config['user']};" +
                              f"Pwd={self.config['password']};")

    def execute(self, sql, params=None):
        with self.getCursor() as cursor:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
        self.commit()

    def execute_query(self, sql, params=None):
        cursor = self.get_connection().cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        return cursor

    def getCursor(self):
        return self.get_connection().cursor()

    def close(self):
        self.get_connection().close()

    def commit(self):
        self.get_connection().commit()