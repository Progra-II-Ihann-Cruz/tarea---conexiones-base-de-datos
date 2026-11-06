class crtlArticulo:

    def __init__(self, adapter):
        self.adapter = adapter

    def insert(self, articulo):
        try:
            aux_sql = "insert into articulos(titulo, cuerpo, id_autor) values(?, ?, ?)"
            parametros = (articulo.titulo, articulo.cuerpo, articulo.id_autor)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def selectAll(self):
        try:
            aux_sql = "select * from articulos"
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

    def selectOne(self, articulo):
        try:
            aux_sql = "select * from articulos where id_articulo = ?"
            parametros = (articulo.id_articulo,)

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

    def update(self, articulo):
        try:
            aux_sql = "update articulos set titulo = ?, cuerpo = ?, id_autor = ? where id_articulo = ?"
            parametros = (articulo.titulo, articulo.cuerpo, articulo.id_autor, articulo.id_articulo)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()

    def delete(self, articulo):
        try:
            aux_sql = "delete from articulos where id_articulo = ?"
            parametros = (articulo.id_articulo,)

            if hasattr(self.adapter, 'execute'):
                self.adapter.execute(aux_sql, parametros)
        except Exception as e:
            raise e
        finally:
            self.adapter.close()