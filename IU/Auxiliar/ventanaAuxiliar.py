import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication


class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()



        self.window.setWindowTitle("AUXILIAR")
        self.window.setGeometry(500,500,600,600)

        self.window.show()
        sys.exit(self.app.exec_())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # asd = IniciarSesion()

    ex = MainWindow()

    # sys.exit(app.exec_())

    app.exec_()