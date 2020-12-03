import sys
from PyQt5 import QtWidgets, uic


def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("example1.ui")
mainwindow_setup(window)
window.show()
app.exec_()
