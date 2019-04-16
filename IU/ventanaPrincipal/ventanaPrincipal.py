import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from IU.InicioSesion.ventanaInicioDeSesion import IniciarSesion


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        #self.imagePath =

        self.initGUI()
        self.nextWindow=None

        self.window.setWindowTitle("MENU PRINCIPAL")
        self.window.setGeometry(500,500,600,600)
        self.window.show()
        sys.exit(self.app.exec_())

    def initGUI(self):

        # crear iniciar sesion button
        self.iniciarSesion = QtWidgets.QPushButton(self.window)
        self.iniciarSesion.setText("iniciar sesion")
        self.iniciarSesion.setGeometry(25, 450, 250, 40)
        self.iniciarSesion.clicked.connect(self.event_iniciarSesion)
        # crear resgistrarse button
        self.registrarse = QtWidgets.QPushButton(self.window)
        self.registrarse.setText("registrarse")
        self.registrarse.setGeometry(25, 510, 250, 40)

    def event_iniciarSesion(self):
        self.nextWindow = IniciarSesion()
        self.window.setVisible(False)
        self.nextWindow.window.setVisible(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
