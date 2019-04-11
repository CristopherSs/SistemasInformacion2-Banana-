"""
    este archivo contiene la clase
    :Curso
"""
from typing import Union


class Curso:
    """
        esta clase tiene la capacidad de poder agregar estudiantes
    """

    def __init__(self, nombre_curso: str, codigo: str, docente: Docente, materia: Materia) -> None:
        self.__noombre_curso = nombre_curso
        self.__codigo = codigo
        self.__docente = docente
        self.__materia = materia
        self.__estudiantes_auxiliares = []

    def registar_usuario(self, codigo: str, usuario: Union[Auxiliar, Estudiante]) -> bool:
        """
            este metodo se encargara de verificar el codigo y que no haya otro usuario
            repetido para no tener conflictos  en la base de datos lo cual los usuarios a registrar
            pueden ser auxiliares o estudiantes

        :param codigo: el codigo que mandara el usuario para hacer la verificaion
        :param usuario: los datos para registrar
        :return: true si se puede y false si existe alguna dificultad
        """
        if self.__codigo is codigo:
            ...

    def actualizar_codigo(self, nuevo_codigo: str) -> None:
        """
            este metodo permite cambiar o actualizar en codigo con el que fue creado o vuelto a cambiar
        :param nuevo_codigo: nuevo valor  a intercambiar
        :return: none
        """
        self.__codigo = nuevo_codigo

