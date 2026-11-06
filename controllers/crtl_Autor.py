class crtlAutor:

    def __init__(self, adapter):
        self.adapter = adapter

    def insert(self, autor):
        try:
            aux_sql = "insert into autor(nombre, apells) values(?, ?)"
            parametros = (autor.nombre, autor.apells)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def selectAll(self):
        try:
            aux_sql = "select * from autor"
            if hasattr(self.adapter, 'execute_query'):
                cursor = self.adapter.execute_query(aux_sql)
            else:
                cursor = self.adapter.getCursor()
                cursor.execute(aux_sql)
            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def selectOne(self, autor):
        try:
            aux_sql = "select * from autor where id_autor = ?"
            parametros = (autor.id_autor,)

            if hasattr(self.adapter, 'execute_query'):
                cursor = self.adapter.execute_query(aux_sql, parametros)
            else:
                cursor = self.adapter.getCursor()
                cursor.execute(aux_sql, parametros)
            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def update(self, autor):
        try:
            aux_sql = "update autor set nombre = ?, apells = ? where id_autor = ?"
            parametros = (autor.nombre, autor.apells, autor.id_autor)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def delete(self, autor):
        try:
            aux_sql = "delete from autor where id_autor = ?"
            parametros = (autor.id_autor,)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()