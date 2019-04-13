"""
    este archivo contiene la subclase de tipo usuario
    :Estudiante
"""
from backend.usuario.usuario import Usuario


class Estudiante(Usuario):
    """
        esta calse simula todas las funcionalidades que
        tendra una entidad Estudiante
    """

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        Usuario.__init__(self, nombres=nombre, apellidos=apellido, email=email, contrasenia=contrasenia)
