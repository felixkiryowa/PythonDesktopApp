from PyQt5 import QtGui
from PyQt5.QtWidgets import (
 QApplication,
 QMainWindow,
 QStatusBar
)
import sys


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("equator.png"))

        self.InitWindow()
    def InitWindow(self):
        self.statusBar().showMessage("This is a status bar")
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())