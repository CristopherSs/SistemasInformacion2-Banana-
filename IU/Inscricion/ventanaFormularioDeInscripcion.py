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

    #crear nombre completo field
        #self.nombreCompleto = QtWidgets.QTextEdit(self.window)
        #self.nombreCompleto.setGeometry(206,158,326,27)
        #self.nombreCompleto.setText("nombre completo")
    #crear carrera field
        #self.carrera = QtWidgets.QTextEdit(self.window)
       # self.carrera.setGeometry(206,211,326,27)
      #  self.carrera.setText("carrera")
    #crear materia field
       # self.materia = QtWidgets.QTextEdit(self.window)
      #  self.materia.setGeometry(206,254,326,27)
     #   self.materia.setText("materia")
    #crear codigo identificador field
        self.codigoIdentificador  = QtWidgets.QTextEdit(self.window)
        self.codigoIdentificador.setGeometry(25, 90, 250, 40)
        self.codigoIdentificador.setText("Codigo identificador")
    #crear inscripcion button
        self.inscribirse = QtWidgets.QPushButton(self.window)
        self.inscribirse.setText("Inscribirse")
        self.inscribirse.setGeometry(25,210, 250, 40)
main = MainWindow()