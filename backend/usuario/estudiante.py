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

    def __init__(self, nombre: str, contrasenia: str) -> None:
        Usuario.__init__(self, nombre, contrasenia)
