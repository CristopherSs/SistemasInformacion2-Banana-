import psycopg2

import psycopg2

class Conexcion:
    def __init__(self)-> None:
        self. = "host='localhost' port='5432' user=postgres password=minipelaez dbname='sistemas2info'"

    def check_connection(self)-> None:
        query = 'select * from food '
        try:
            self.__cons = psycopg2.connect(self.connstr)
            self.__cur  = self.__cons.cursor()
        except psycopg2.ProgrammingError:
            ptint("connection not established")
        finally:
            print("finish")
    def consult_database(self,query : str )-> None:
        try:
            self.__cons = psycopg2.connect(self.connstr)
            #self.__cons.autocommit = false
            self.__cur = self.__cons.cursor()
            self.__cur.execute(query)
        except psycopg2.ProgrammingError:
            print("failures in the database")
            self.__cons.rollback()
        finally:
            self.__cons.commit()
            self.__cur.close()
            self.__cons.close()

    def insert_database(self , name_food :str  ) -> None :
        insert = 'INSERT INTO public."food"(id_food ,name_food)VALUES (9,'+"'"+name_food+"'"+');'
        self.consult_database(insert)