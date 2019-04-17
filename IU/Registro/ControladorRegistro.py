

from backend.usuario.usuario import *
from IU.ventanaPrincipal.ventanaPrincipal import *

class registrar:

    def __init__(self):
        self.usr = Usuario
        self.w = MainWindow
        self.reg = registrarse

    def v_login(self):
        self.w.__init__()
        if(self.w.event_registrarse()):
            self.reg.__init__(self)

    def regUser(self,nombre:str, apellido:str,email:str, contraeña : str):
        ...



#este metodo registrara a un usuario en una respectiva categoria(estudiante,docente,auxiliar
