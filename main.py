from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget, QTreeWidgetItem, QMessageBox
from ui_login import Ui_Login
from ui_main_window import Ui_main_window
from database import DataBase
import sys
import pandas as pd
import sqlite3
from PySide2 import QtCore
from xml_files import Read_xml
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt

class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 1
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.open_system)   

    def open_system(self):
      #Login no sistema
      db = DataBase()
      db.conecta()   
      autorizado = db.login_user(self.txt_user.text(), self.txt_pass.text())

      if autorizado:
        self.w = MainWindow(db.check_user(self.txt_user.text(), self.txt_pass.text()))
        self.w.show()
        self.close()
      else:
        if self.tentativas < 3:
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Warning)
          msg.setWindowTitle("Login ou senha inválida")
          msg.setText(f"Usuário ou senha inválida\nTentativa {self.tentativas} de 3")
          msg.exec_()
          self.tentativas += 1
        else:
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Warning)
          msg.setWindowTitle("Login ou senha inválida")
          msg.setText(f"Tentativa {self.tentativas} de 3\nO sistema será encerrado!\nCaso tenha esquecido sua senha, favor contatar o administrador do sistema.")
          msg.exec_()
          db.close_connection()
          sys.exit(0) 

class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self, user):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.setWindowTitle("Tela Principal")
      self.user = 'bryan'

      if user.lower() != 'administrador':
        self.btn_main_cadastrar_usuario.setVisible(False)

    #Botões navegação
      self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_home))
      self.btn_main_cadastrar_usuario.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_cadastro))
      self.btn_tables.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_tables))
      self.btn_importar.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_import))
      self.btn_sobre.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_sobre))
      self.btn_contatos.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_contato))
      self.btn_clientes.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_cliente_cadastro))

      self.btn_cadsatrar_usuario.clicked.connect(self.subscribe_user)

      self.btn_open_path.clicked.connect(self.open_path)
      self.btn_import.clicked.connect(self.import_xml_files)
      self.reset_table()
      self.lineedit_estoque.textChanged.connect(self.update_filter)

      self.btn_saida.clicked.connect(self.gerar_saida)
      self.btn_entrada.clicked.connect(self.gerar_estorno)
      self.btn_gerar_excel.clicked.connect(self.excel_file)
      self.btn_gerar_grafico.clicked.connect(self.graphic)

    def subscribe_user(self):
      if self.txt_senha.text() != self.txt_senha2.text():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Senhas Divergentes!")
        msg.setText("As senhas não são compatíveis.")
        msg.exec_()
        return None
      elif len(self.txt_senha.text()) < 8 or self.txt_nome.text() == '':
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

    def table_cliente(self):
        self.tableView_estoque.setStyleSheet("QHeaderView{ color:white, font-size: 15px;}")
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tableView_cliente.setModel(self.model)
        self.model.setTable("cliente")
        self.model.select()


    def table_estoque(self):
      self.tw_estoque.setStyleSheet("QHeaderView{ color:white, font-size: 15px;}")

      cn = sqlite3.connect('system.db')
      result = pd.read_sql_query("SELECT * FROM notas WHERE data_saida = ''", cn)
      result = result.values.tolist()

      self.x = ''

      for i in result:
        if i[0] ==self.x:
          QTreeWidgetItem(self.campo, i)
        else:
          self.campo = QTreeWidgetItem(self.tw_estoque, i)
          self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

        self.x = i[0]
      
      self.tw_estoque.setSortingEnabled(True)

      for i in range(1,15):
        self.tw_estoque.resizeColumnToContents(i)
    
    def table_saida(self):
      self.tw_saida.setStyleSheet("QHeaderView{ color:white, font-size: 15px;}")

      cn = sqlite3.connect('system.db')
      result = pd.read_sql_query("SELECT NFe, descricao, unidade_medida, quantidade, usuario FROM notas WHERE data_saida <> ''", cn)
      result = result.values.tolist()

      self.x = ''

      for i in result:
        if i[0] ==self.x:
          QTreeWidgetItem(self.campo, i)
        else:
          self.campo = QTreeWidgetItem(self.tw_saida, i)
          self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

        self.x = i[0]
      
      self.tw_saida.setSortingEnabled(True)

      for i in range(1,15):
        self.tw_saida.resizeColumnToContents(i)

    def table_geral(self):

        self.tableView_estoque.setStyleSheet("QHeaderView{ color:white, font-size: 15px;}")
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tableView_estoque.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    def open_path(self):
      self.path = QFileDialog.getExistingDirectory(self, str("Open Directory"),"/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
      self.txt_file.setText(self.path)

    def import_xml_files(self):
      xml = Read_xml(self.txt_file.text())
      all = xml.all_files()
      self.progressBar.setMaximum(len(all))

      db = DataBase()
      db.conecta()

      count = 1

      for i in all:
        self.progressBar.setValue(count)
        fullDataSet = xml.nfe_data(i)
        db.insert_data(fullDataSet)
        count += 1
      
      msg = QMessageBox()
      msg.setWindowTitle("Importação XML")
      msg.setText("Importação Concluída!")
      msg.exec_()
      self.progressBar.setValue(0)

      db.close_connection()
      self.reset_table()

    def update_filter(self, s):
      s = re.sub("[\W_]+", "", s)
      filter_str = 'NFe LIKE "%{}%"'.format(s)
      self.model.setFilter(filter_str)

    def gerar_saida(self):

        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))
    
        recurse(self.tw_estoque.invisibleRootItem())

        #Pergunta se usuario realmente deseja fazer isos.
        self.question('saída')

    def gerar_estorno(self):
        
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))
                                                      
        recurse(self.tw_saida.invisibleRootItem())
        self.question('estorno')      

    def question(self, table):

        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText("As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    def excel_file(self):
      cnx = sqlite3.connect('system.db')
      result = pd.read_sql_query("SELECT * FROM notas", cnx)
      result.to_excel("Resumo de notas.xlsx", sheet_name='Notas', index=False)

      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle("Relatório de Notas")
      msg.setText("Relatório gerado com sucesso!")
      msg.exec_()

    def graphic(self):

        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query('SELECT * FROM notas', cnx)
        saida = pd.read_sql_query("SELECT * FROM notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())