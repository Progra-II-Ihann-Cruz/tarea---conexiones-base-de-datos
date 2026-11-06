from factory.MySqlAdapter import MySqlAdapter
from factory.MSQLSvrAdapter import MSQLSvrAdapter
from factory.PostgreSQLAdapter import PostgreSQLAdapter
from utils.DBType import DBType

class Factory:

    def __init__(self, adapter):
        self.adapter = adapter

    def create(self, dbType):
        if dbType == DBType.MySQL:
            self.adapter = MySqlAdapter(self.adapter)
        elif dbType == DBType.MSSQL:
            self.adapter = MSQLSvrAdapter(self.adapter)
        elif dbType == DBType.PostgreSQL:
            self.adapter = PostgreSQLAdapter(self.adapter)
        else:
            self.adapter = None

        return self.adapter