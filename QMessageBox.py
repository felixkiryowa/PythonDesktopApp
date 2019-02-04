from PyQt5 import QtGui
from PyQt5.QtWidgets import (
 QApplication,
 QMainWindow,
QMessageBox,
QPushButton
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
        button = QPushButton("About Box", self)
        button.move(200, 200)
        button.clicked.connect(self.AboutMessage)

        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def AboutMessage(self):
        QMessageBox.about(self, "About Message", "This is About Message Box")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())