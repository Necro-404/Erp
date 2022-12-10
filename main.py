from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QTreeWidgetItem, QMessageBox
from ui_login import Ui_Login
from ui_main_window import Ui_main_window
from database import DataBase
import sys
import pandas as pd
import sqlite3
from PySide2 import QtCore


class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.open_system)
        

    def open_system(self):
      #Login no sistema
      db = DataBase()
      db.conecta()
      if db.login_user(self.txt_user.text().lower(), self.txt_pass.text()):
        self.w = MainWindow(db.check_user(self.txt_user.text().lower(), self.txt_pass.text()))
        self.w.show()
        self.close()
      else:
        print("Senha inválida!")
      db.close_connection()
      #Fim Login no sistema
   

class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self, user):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.setWindowTitle("Tela Principal")

      if user.lower() != 'administrador':
        self.btn_main_cadastrar_usuario.setVisible(False)

    #Botões navegação
      self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_home))
      self.btn_tables.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_tables))
      self.btn_main_cadastrar_usuario.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_cadastro))
      self.btn_sobre.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_sobre))
      self.btn_contatos.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_contato))

      self.btn_cadsatrar_usuario.clicked.connect(self.subscribe_user)

      self.table_estoque()

    def subscribe_user(self):
      if self.txt_senha.text() != self.txt_senha2.text():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Senhas Divergentes!")
        msg.setText("As senhas não são compatíveis.")
        msg.exec_()
        return None
      elif len(self.txt_senha.text()) <8:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("A senha deve conter ao menos 8 caracters!")
        msg.setText("A senha deve conter ao menos 8 caracters!")
        msg.exec_()
      else:     
        nome = self.txt_nome.text() 
        user = self.txt_usuario.text()  
        password = self.txt_senha.text() 
        access = self.combobox_perfil.currentText() 

        print(nome,user,password,access)
        db = DataBase()
        db.conecta()

        db.insert_user(nome,user,password,access)

        db.close_connection

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro realizado com sucesso")
        msg.setText("Cadastro realizado com sucesso")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha2.setText("")

    def table_estoque(self):
      self.tw_estoque.setStyleSheet("color:#fff; font-size: 15px;")
      self.tw_estoque.setStyleSheet("QHeaderView{ color:black}")

      cn = sqlite3.connect('system.db')
      result = pd.read_sql_query("SELECT * FROM users", cn)
      result = result.values.tolist()
      print(result)


      self.x = ''

      for i in result:
        self.campo = QTreeWidgetItem(self.tw_estoque, i)
        self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

      self.x = i[0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())