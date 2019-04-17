from IU.Inscricion.ventanaFormularioDeInscripcion import *
from backend.usuario.usuario import *
from backend.curso.curso import *


class incripcion:
    def  __init__(self):
        self.vent = codigoInscripcion
        self.usr = Usuario
        self.curso = Curso
    def in_(self, cod: str, ) -> None:
        self.curso.registar_usuario(cod,usr)

