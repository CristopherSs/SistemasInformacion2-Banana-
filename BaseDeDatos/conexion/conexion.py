import psycopg2
import json

class Conexion:
    def __init__(self ) -> None:
        #self.__conex = "host=%s port=%s user=%s password=%s dbaname=%s" %(self.__PSQL_HOST,self.__PSQL_PORT,self.__PSQL_USER,self.__PSQL_PASS,self.__PSQL_DB)
        self.__connstr = "host='localhost' port='5432' user=postgres password=minipelaez dbname='Prueba'"
        with open('SistemasInformacion2/BaseDeDatos/config.json', 'r') as file:
            config = json.load(file)
        #self.__connstr = "host={2} port={3} user={0} password={1} dbname={4}"
        """conexcion utilizando libreria psycopg2 devuelve la 
            conexion para las otras clases reutili...."""
    def conectar(self) -> None:
        try:
            conectar = psycopg2.connect(self.__connstr)
            curs = conectar.cursor()
            print (type(conectar))
        except psycopg2.ProgrammingError:
            print("no se pudo conectar  con la base de datos")
        finally:
            #conectar.commit()
            #curs.close()
            #conectar.close()
            print("esperando")
        return conectar

if __name__ == "__main__":
    config = {'user': 'root', 'password': '', 'database': '', 'host': ''}
    conexion = Conexion()