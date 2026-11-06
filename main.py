from utils.DBType import DBType
from factory.DBAdapterFactory import Factory
from entities.cls_Autor import Autor
from entities.cls_Articulo import Articulo
from controllers.crtl_Autor import crtlAutor
from controllers.crtl_Articulo import crtlArticulo
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    dataConnection = {'host':  os.environ.get('HOST'),
                      'user':  os.environ.get('USER'),
                      'password': os.environ.get('PASSWORD'),
                      'database': os.environ.get('DATABASE')}

    try:
        conex = Factory(dataConnection).create(DBType.PostgreSQL)
        conex.getCursor()
        conex.close()
    except Exception as e:
        print(e)
    else:
        print('Conexión exitosa')

    try:
        autor = Autor(0, 'Merlina', 'Addams')
        crtlAutor(Factory(dataConnection).create(DBType.PostgreSQL)).insert(autor)
    except Exception as e:
        print(e)
    else:
        print('Insert exitoso')

    try:
        resu = crtlAutor(Factory(dataConnection).create(DBType.PostgreSQL)).selectAll()
        for tupla in resu:
            if type(tupla) == dict:
                autor = Autor(tupla['id_autor'], tupla['nombre'], tupla['apells'])
            else:
                autor = Autor(tupla[0], tupla[1], tupla[2])
            print('ID: ', autor.id_autor, '  Nombre: ', autor.nombre, '', autor.apells)

    except Exception as e:
        print(e)
    else:
        print('Select all exitoso')

    try:
        autor = Autor(1, 'Wednesday', 'Addams')
        crtlAutor(Factory(dataConnection).create(DBType.PostgreSQL)).update(autor)
    except Exception as e:
        print(e)
    else:
        print('Update exitoso')

    try:
        articulo = Articulo(0, 'Mi primer articulo', 'Cuerpo del articulo', 1)
        crtlArticulo(Factory(dataConnection).create(DBType.PostgreSQL)).insert(articulo)
    except Exception as e:
        print(e)
    else:
        print('Insert articulo exitoso')

    try:
        resu = crtlArticulo(Factory(dataConnection).create(DBType.PostgreSQL)).selectAll()
        for tupla in resu:
            if type(tupla) == dict:
                articulo = Articulo(tupla['id_articulo'], tupla['titulo'], tupla['cuerpo'], tupla['id_autor'], tupla['fecha'])
            else:
                articulo = Articulo(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
            print('ID: ', articulo.id_articulo, '  Titulo: ', articulo.titulo, '  Autor: ', articulo.id_autor, '  Fecha: ', articulo.fecha)
    except Exception as e:
        print(e)
    else:
        print('Select all articulos exitoso')

    try:
        articulo = Articulo(1, '', '', 0)
        print(crtlArticulo(Factory(dataConnection).create(DBType.PostgreSQL)).selectOne(articulo))
    except Exception as e:
        print(e)
    else:
        print('Select one articulo exitoso')

    try:
        articulo = Articulo(1, 'Titulo modificado', 'Cuerpo modificado', 1)
        crtlArticulo(Factory(dataConnection).create(DBType.PostgreSQL)).update(articulo)
    except Exception as e:
        print(e)
    else:
        print('Update articulo exitoso')

    try:
        articulo = Articulo(1, '', '', 0)
        crtlArticulo(Factory(dataConnection).create(DBType.PostgreSQL)).delete(articulo)
    except Exception as e:
        print(e)
    else:
        print('Delete articulo exitoso')

    try:
        autor = Autor(1, '', '')
        crtlAutor(Factory(dataConnection).create(DBType.PostgreSQL)).delete(autor)
    except Exception as e:
        print(e)
    else:
        print('Delete exitoso')