from backend.usuario.usuario import Usuario
from IU.ventanaPrincipal.ventanaPrincipal import *
from IU.InicioSesion.ventanaInicioDeSesion import *
from IU.Estudiante.ventanaEstudiante import *
from IU.Docente.VentanaDocente import *



class Sesion:

    def __abs__(self, login: str, contras: str ):
        self.user = login
        self.psw= contras
        self.window = MainWindow
        self.sesion = IniciarSesion
        self.usr = Usuario
        self.docente = MainWindow
        self.estudiante = MainWindow
    def v_login(self)-> bool:
        self.window.__init__()
        if(self.window.event_iniciarSesion()):
            self.sesion()

    def sesion(self):
        self.sesion.__init__()
        self.verificar(self)
        tipo = self.setTpoUser()
        if ( tipo== 'docente') :
                self.docente.__init__()
        else:
            if (tipo == 'estudiante'):
                self.estudiante.__init__()


    def verificar(self) -> str:
            #self.usr.verificar()
            consulta = 'SELECT * FROM usuario WHERE nombre = ' + "'" + self.user + "'" + 'and pasword = ' + "'" + self.psw + "'" + ';  '
            tipo = self.tipoUser(consulta)
            return tipo

    def setTpoUser(self) -> str:

        "Este metodo hara una consulta que buscara el rol del usuario"
        return "tipoUsuario"