import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt



class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        #self.imagePath =

        self.initGUI()

        self.window.setWindowTitle("FORMULARIO DE INSCRIPCION")
        self.window.setGeometry(500,100,300,300)
        self.window.show()
        sys.exit(self.app.exec_())

    def initGUI(self):


    #crear codigo identificador field
        self.codigoIdentificador  = QtWidgets.QTextEdit(self.window)
        self.codigoIdentificador.setGeometry(25, 90, 250, 40)
        self.codigoIdentificador.setText("Codigo identificador")
    #crear inscripcion button
        self.inscribirse = QtWidgets.QPushButton(self.window)
        self.inscribirse.setText("Inscribirse")
        self.inscribirse.setGeometry(25,210, 250, 40)
main = MainWindow()