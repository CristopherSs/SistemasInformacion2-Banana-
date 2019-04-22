from backend.usuario.usuario import Usuario
from BaseDeDatos.conexion.conexion import Conexion
import psycopg2

class GeradorUs:
    def __init__(self):
        self.__conexion = Conexion()

    def crear_tbusuario(self):
        table_user = usuario
        diccionario = table_user .__dict__
        #print(diccionario)
        #cadena  = 'CREATE TABLE {_Usuario__nombre_completo} {_Usuario__apodo_id} {_Usuario__email} {_Usuario__contrasenia}'.format(**diccionario)
        #print(type(table_user).__name__ )
        keys = list(diccionario.keys())
        cadena = 'CREATE TABLE({0},{1},{2},{3})'.format(*keys)
        print(keys)
        print(type(keys))
        nombre_tabla = type(table_user).__name__
        print(cadena)
        #print(diccionario)
        #print(nombre_tabla)

        create =  'CREATE TABLE '+nombre_tabla+'(_User_id serial PRIMARY KEY ,{0}  character(20), {1} character(20), {2}  VARCHAR(20), {3}  VARCHAR(20));'.format(*list(diccionario.keys()))
        #cretwo = "Create table "+nombre_tabla +"({1},{1},{2},{3})".format(**dict(list(diccionario.keys())))
        print(create)
        try:
            conectar = conexion.conectar()
            cursor = conectar.cursor()
            cursor.execute(create)
        except psycopg2.ProgrammingError:
            print("no se pudo conectar  con la base de datos")
        finally:
            conectar.commit()
            cursor.close()
            conectar.close()

    def eliminar_usuario(self, email_usuario : str ):
        consulta = "DELETE FROM Usuario WHERE  _usuario_email ="+"'"+email_usuario+"'"+";"
        try:
            conectar = conexion.conectar()
            cursor  = conectar.cursor()
            cursor.execute(consulta)
        except psycopg2.ProgrammingError:
            print("no se pudo conectar  con la base de datos")
        finally:
            conectar.commit()
            cursor.close()
            conectar.close()
    def ingresar_usuario(self):
        consulta = 'INSERT INTO usuario(id_usuario, apodo_usuario, sontrasena_usuario, email_usuario)VALUES (2,'+"'ees'"+",'sasd','sada');"
        try:
            conectar = conexion.conectar()
            cursor = conectar.cursor()
            cursor.execute(consulta)
        except psycopg2.ProgrammingError:
             print("no se pudo conectar  con la base de datos")
        finally:
            conectar.commit()
            cursor.close()
            conectar.close()
    def buscar_usuario(self , apodo : str) -> bool:
        consulta =  'SELECT  id_usuario FROM  Usuario  WHERE apodo_usuario = '+"'"+apodo+"'"+';'
        try:
            conectar = conexion.conectar()
            cursor = conectar.cursor()
            cursor.execute(consulta)
            ccur = cursor.fetchone()
        except psycopg2.ProgrammingError:
            print("no se pudo conectar  con la base de datos")
            ccur = False
        finally:
            conectar.commit()
            cursor.close()
            conectar.close()
        return ccur

    def actualizar_usuario(self , apodo :str ,contrasena : str , email : str):
        #consulta  =  'UPDATE public."Usuario"SET apodo_usuario = '+"'"+apodo+"',sontrasena_usuario = "+"'"+contrasena+"' WHERE email_usuario = "+"'"+email+';
        try:
            conectar = conexion.conectar()
            cursor = conectar.cursor()
            cursor.execute(consulta)
        except psycopg2.ProgrammingError:
            print("no se pudo conectar  con la base de datos")
            ccur = False
        finally:
            conectar.commit()
            cursor.close()
            conectar.close()


if __name__ == "__main__":
    usuario =  Usuario('jason','choque','jsoao@s','pers')
    genredor = GeradorUs()
    conexion = Conexion()
    genredor.crear_tbusuario()
    #genredor.ingresar_usuario();
    #print(genredor.buscar_usuario('perro'))
    #genredor.actualizar_usuario('paloma','paloma13','sada')