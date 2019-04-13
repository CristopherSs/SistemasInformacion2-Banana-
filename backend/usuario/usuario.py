"""
    este archivo contiene la clase base
    :Usuario
"""


class Usuario:

    def __init__(self, nombre: str, contrasenia: str) -> None:
        self.__nombre = nombre
        self.__contrasenia = contrasenia

    def obtener_nombre(self) -> str:
        """
            devuelve el nombre ya que es privado
        :return: self.__nombre -> str
        """
        return self.__nombre

    def obtener_contrasenia(self) -> str:
        """
            devuelve la contrasenia ya que es privado
        :return: self.__contrasenia -> str
        """
        return self.__contrasenia

    def actualizar_nombre(self, nuevo_nombre: str) -> None:
        """
            modifica el nombre actual
        :param nuevo_nombre: valor a cambiar
        :return: none
        """

        self.__nombre = nuevo_nombre

    def actualizar_contrasenia(self, nueva_contrasenia: str) -> None:
        """
            modifica la contrasenia actual
        :param nueva_contrasenia: valor a cambiar
        :return: none
        """

        self.__contrasenia = nueva_contrasenia

    def __eq__(self, otro: 'Usuario') -> bool:
        """
            este metodo verifica si otro objeto del mismo tipo es igual en sus atributos
            importantes :v
        :param other: un objeto de tipo Usuario a verificar
        :return: true si es igual y false si no lo es
        """
        return otro.__nombre is self.__nombre
