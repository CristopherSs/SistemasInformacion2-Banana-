import psycopg2


class   Connection:
        def __init__(self)-> None:
            self.__connstr = "host='localhost' port='5432' user=postgres password=minipelaez dbname='postgres'"

        def verificar(self, consulta   : str) -> None:
            pass
        def guardar(self, consulta : str) -> None:
            pass

        def ejecutar_consultas(self, consulta : str) -> None:
            pass

        def crear_tabla(self,consulta : str )-> None:
            pass

if __name__=='__main__':
    connection = Connection()
    connection.verifyes('banana')
    connection.save('banana')

