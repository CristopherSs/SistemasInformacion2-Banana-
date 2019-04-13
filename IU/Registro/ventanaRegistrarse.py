import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt



class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        #self.imagePath =

        self.initGUI()

        self.window.setWindowTitle("REGISTRARSE")
        self.window.setGeometry(500,100,300,600)
        self.window.show()
        sys.exit(self.app.exec_())

    def initGUI(self):

    #crear nick field
        self.nick = QtWidgets.QTextEdit(self.window)
        self.nick.setGeometry(25,90,250,40)
        self.nick.setText("nick")

    # crear nombres field
        self.nombre = QtWidgets.QTextEdit(self.window)
        self.nombre.setGeometry(25, 150, 250, 40)
        self.nombre.setText("nombre(s)")
    # crear apellido field
        self.apellido = QtWidgets.QTextEdit(self.window)
        self.apellido.setGeometry(25, 210, 250, 40)
        self.apellido.setText("apellido(s)")
    #crear email field
        self.email = QtWidgets.QTextEdit(self.window)
        self.email.setGeometry(25, 270, 250, 40)
        self.email.setText("email")
    #crear contrasenia field
        self.contrasenia = QtWidgets.QTextEdit(self.window)
        self.contrasenia.setGeometry(25, 330, 250, 40)
        self.contrasenia.setText("contrasenia")
    #crear confirmarContrasenia field
        self.confirmarContrasenia  = QtWidgets.QTextEdit(self.window)
        self.confirmarContrasenia.setGeometry(25, 390, 250, 40)
        self.confirmarContrasenia.setText("Confirmar Contrasenia")
    #crear resgistrarse button
        self.registrarse = QtWidgets.QPushButton(self.window)
        self.registrarse.setText("resgistrarse")
        self.registrarse.setGeometry(25, 510, 250,40)
main = MainWindow()