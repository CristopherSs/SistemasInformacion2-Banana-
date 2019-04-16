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
        self.nombreMateria  = QtWidgets.QTextEdit(self.window)
        self.nombreMateria.setGeometry(25, 90, 250, 40)
        self.nombreMateria.setText("Nombre Materia")
    #crear inscripcion button
        self.codigo = QtWidgets.QPushButton(self.window)
        self.codigo.setText("Generar Codigo Identificador")
        self.codigo.setGeometry(25,210, 250, 40)
main = MainWindow()