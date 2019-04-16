import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt



class IniciarSesion(QtWidgets.QMainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        #self.imagePath =

        self.initGUI()

        self.window.setWindowTitle("INICIAR SESION")
        self.window.setGeometry(500,100,300,300)
        self.window.setVisible(True)
        self.window.show()

        # sys.exit(self.app.exec_())
        # self.app.exec_()

    def initGUI(self):

    #crear correo field
        self.correo = QtWidgets.QTextEdit(self.window)
        self.correo.setGeometry(25,90,250,40)
        self.correo.setText("Correo Electronico")

    # crear contrasenia field
        self.contrasenia = QtWidgets.QTextEdit(self.window)
        self.contrasenia.setGeometry(25, 150, 250, 40)
        self.contrasenia.setText("Contrasenia")


    # crear resgistrarse button
        self.iniciarSesion = QtWidgets.QPushButton(self.window)
        self.iniciarSesion.setText("Iniciar Sesion")
        self.iniciarSesion.setGeometry(25,210, 250, 40)


# am= IniciarSesion()