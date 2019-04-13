"""
    este archivo contiene la clase base
    :Usuario
"""
from copy import copy


class Usuario:
    """
        esta clase es base para las que vayan a heredar y puedan ser de tipo usuario
    """

    def __init__(self, nombres: str, apellidos: str, email: str, contrasenia: str) -> None:
        self.__nombre_completo = self.__acoplar_nombre(nombres, apellidos)
        self.__apodo_id = self.__generar_apodo(nombres, apellidos)
        self.__email = email
        self.__contrasenia = contrasenia

    def obtener_nombre_completo(self) -> str:
        """
            devuelve el nombre ya que es privado
        :return: self.__nombre_completo -> str
        """
        return copy(self.__nombre_completo)

    def obtener_contrasenia(self) -> str:
        """
            devuelve la contrasenia ya que es privado
        :return: self.__contrasenia -> str
        """
        return copy(self.__contrasenia)

    def obtener_apodo(self) -> str:
        """
        devuelde una copia del apodo
        :return: self.__apodo
        """
        return copy(self.__apodo_id)

    def actualizar_nombre(self, nombre: str, apellidos: str) -> None:
        """
            se actualizara la variable self.__nombre_completo
        :param nombre: nuevo nombre a cambiar
        :param apellidos: nuevo apellido a cambiar
        :return: nombre contruido
        """
        self.__nombre_completo = self.__acoplar_nombre(nombre, apellidos)
        self.__apodo_id = self.__generar_apodo(nombre, apellidos)

    def obtener_email(self) -> str:
        """
            devuelve copia del emai
        :return: user@gmail.com
        """
        return copy(self.__email)

    def actualizar_emai(self, emai: str) -> None:
        """
            modificar el emai actual
        :param emai: nuevo emai
        :return: none
        """

        self.__email = emai

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
        return otro.__nombre_completo is self.__nombre_completo

    def __generar_apodo(self, nombre: str, apellido: str) -> str:
        """
            este metodo genera automaticamente un apodo al usuario
        :param nombre: nombre del usuario
        :param apellido: apellido del usuario
        :return: una cadena construida con los parametros
        """
        nombre = nombre + ' '
        apellido = apellido + ' '
        return nombre[0:nombre.find(' ') - 1] + apellido[0:apellido.find(' ') - 1]

    def __acoplar_nombre(self, nombre: str, apellido: str) -> str:
        """
            usa librerias para unir correctamente el nombre
        :param nombre: nuevo
        :param apellido: nuevo
        :return: cadena construida
        """
        return "%s %s" % (nombre, apellido)
