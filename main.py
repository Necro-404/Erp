from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from ui_login import Ui_Login
from ui_main_window import Ui_main_window
import sys


class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):
      #Login no sistema
      if self.txt_user.text() == 'admin' and self.txt_pass.text() == '123':
        self.w = MainWindow()
        self.w.show()
        self.close()
      else:
        print("Senha inválida!")
      #Fim Login no sistema
   

class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.setWindowTitle("Tela Principal")

    #Botões navegação
      self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_home))
      self.btn_tables.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_tables))
      self.btn_cadastro.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_cadastro))
      self.btn_sobre.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_sobre))
      self.btn_contatos.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_contato))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())