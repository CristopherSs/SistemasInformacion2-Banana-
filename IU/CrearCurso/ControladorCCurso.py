from backend.usuario.usuario import *
from backend.curso.curso import *
from backend.usuario.docente import *
from IU.CrearCurso.VentanaCrearCurso import *


class creaCurso:

    def __abs__(self, login: str, contras: str):
        self.curso = Curso
        self.docent = Docente
        self.crear = CrearCurso
        self.usr = Usuario

    def creador(self, nomCurso: str, codCurso: int, nomMateria: str):
        docent = self.usr.obtener_nombre_completo(self)
        self.crear.__init__(nomCurso,codCurso,docent,nomMateria)

