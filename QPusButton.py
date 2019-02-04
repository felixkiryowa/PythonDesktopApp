from PyQt5 import QtGui
from PyQt5.QtWidgets import (
 QApplication,
 QMainWindow,
 QPushButton,
 QMessageBox
)
from PyQt5.QtCore import  QCoreApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.title = "PyQt5 Q Push Button"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("equator.png"))
        button = QPushButton("close", self)
        button.move(200, 200)
        button.setToolTip("<h3 style='color:red;'>click this button</h3>")
        # button.clicked.connect(self.close)
        button.clicked.connect(self.CloseApp)
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def CloseApp(self):
        reply = QMessageBox.question(self, "Close Message", "Are You Sure To Close  Window?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())