from enum import Enum

class DBType(Enum):
    MySQL = 1
    MSSQL = 2
    PostgreSQL = 3

    DBType = Enum('DBType', ['MySQL', 'MSSQL'])