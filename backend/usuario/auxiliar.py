"""
    este archivo contiene la subclase de tipo usuario
    :Auxiliar
"""
from backend.usuario.usuario import Usuario


class Auxiliar(Usuario):
    """
        esta calse simula todas las funcionalidades que
        tendra una entidad auxiliar
    """

    def __init__(self, nombre: str, contrasenia: str) -> None:
        Usuario.__init__(self, nombre, contrasenia)

