from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide2.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My ERP")

        self.button = QPushButton("Clique Aqui")

        self.setCentralWidget(self.button)

        self.button.clicked.connect(self.clicked_button)

    def clicked_button(self):
        print('Botão Clicado')
        self.button.setEnabled(False)
        self.setWindowTitle("Just one Click")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
