import sys
from PyQt5 import QtWidgets,QtCore, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from IU.CrearCurso.VentanaCrearCurso import CrearCurso

class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        #self.imagePath =

        self.initGUI()
        # self.nextWindow=MainWindow()


        self.window.setWindowTitle("DOCENTE")
        self.window.setGeometry(500,500,600,600)
        self.window.setVisible(True)

        self.window.show()
        sys.exit(self.app.exec_())

    def initGUI(self):

        # crear crear curso button
        self.creacurso = QtWidgets.QPushButton(self.window)
        self.creacurso.setText("CREAR CURSO")
        self.creacurso.setGeometry(25, 510, 250, 40)
        self.creacurso.clicked.connect(self.event_crearcurso)

    def event_crearcurso(self):




        self.nextWindow = CrearCurso()
        self.window.setVisible(False)
        self.nextWindow.window.setVisible(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # asd = IniciarSesion()

    ex = MainWindow()

    # sys.exit(app.exec_())

    app.exec_()