class Articulo:

    def __init__(self, id_articulo, titulo, cuerpo, id_autor, fecha = None):
        self.id_articulo = id_articulo
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.id_autor = id_autor
        self.fecha = fecha