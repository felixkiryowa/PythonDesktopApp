from PyQt5.QtWidgets import (
  QApplication, QLabel, QDialog, QHBoxLayout, QLineEdit, QPushButton, QGridLayout
)
import  sys

class Helloworld(QDialog):
    # Overridimg the QDialog constructor
    def __init__(self):
        QDialog.__init__(self)
        # layout = QHBoxLayout()
        layout = QGridLayout()
        self.label = QLabel('Hello world !')
        line_edit = QLineEdit()
        button = QPushButton('close')

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)
        # closing the window event
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)
        # Instruct the constructor to use this layout
        self.setLayout(layout)

    def changeTextLabel(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
# label = QLabel('Hello world')
# label.show()
dialog = Helloworld()
dialog.show()
app.exec_()

