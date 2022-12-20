import sqlite3

class DataBase():
  def __init__(self, name = "system.db"):
    self.name = name

  def conecta(self):
    self.connection = sqlite3.connect(self.name)

  def close_connection(self):
    try:
      self.connection.close()
    except:
      pass

  def create_table_users(self):
    try:
      cursor = self.connection.cursor()
      cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          user TEXT UNIQUE NOT NULL,
          password TEXT NOT NULL,
          access TEXT NOT NULL
        );

      """)
    except:
      print("Faça a conexão com o banco")

  def insert_user(self, name, user, password, access):
    try:
      cursor = self.connection.cursor()
      cursor.execute("INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)", (name, user, password, access))
      self.connection.commit()
    except:
      print("Faça a conexão com o banco")

  def login_user(self, user, password):
    try:
      cursor = self.connection.cursor()
      cursor.execute("SELECT * FROM users;")
      print(user, password)

      for linha in cursor.fetchall():
        if linha[2] == user and linha[3] == password:
          return True
        else:
          continue
      return False
    except:
      print("Erro")

  def check_user(self, user, password):
    try:
      cursor = self.connection.cursor()
      cursor.execute("SELECT * FROM users WHERE users.user = (?)",(user,))

      for linha in cursor.fetchall():
        if linha[2] == user and linha[3] == password :
          return linha[4].upper()
        elif linha[2] == user and linha[3] != password :
          return 'senha incorreta'
        else:
          continue
      return "Sem acesso"
    except:
      print("Erro")

  def delete_user(self, user, password):
    try:
      cursor = self.connection.cursor()
      cursor.execute("DELETE FROM users WHERE users.user = (?) and users.password = (?)",(user, password))
      print(user, password)
    except:
      print("Erro")

  def insert_data(self, xml):
    cursor = self.connection.cursor()

    campos_tabela = (
            'NFe','serie','data_emissao','chave','cnpj_emitente','nome_emitente',
             'valorNfe','itemNota','codigo','quantidade','descricao','unidade_medida','valor_produto',
             'data_importacao','usuario','data_saida' )  
    qntd = ','.join(map(str, '?'*16))
    
    query = f"""INSERT INTO notas {campos_tabela} VALUES ({qntd})"""

    try:
      for nota in xml:
        cursor.execute(query, tuple(nota))
        self.connection.commit()
    except:
      print("Nota existe no banco")
    
  def create_table_nfe(self):

      cursor = self.connection.cursor()
      cursor.execute("""

        CREATE TABLE IF NOT EXISTS notas(
          NFe TEXT,
          serie TEXT,
          data_emissao TEXT,
          chave TEXT, 
          cnpj_emitente TEXT, 
          nome_emitente TEXT, 
          valorNfe TEXT,
          itemNota TEXT, 
          codigo TEXT, 
          quantidade TEXT, 
          descricao TEXT, 
          unidade_medida TEXT, 
          valor_produto TEXT, 
          data_importacao TEXT,
          usuario TEXT, 
          data_saida TEXT,
        PRIMARY KEY(chave, NFe, itemNota)
        );

      """)

  def update_estoque(self, data_saida, user, notas):
    try:
      cursor = self.connection.cursor()
      for nota in notas:
        cursor.execute(f"UPDATE notas SET data_saida = '{data_saida}', usuario = '{user}' WHERE NFe = '{nota}'")
        self.connection.commit()
    except:
      raise ValueError("Erro ao conectar no banco")
  
  def update_estorno(self, notas):

        try:
            cursor = self.connection.cursor()

            for nota in notas:
                cursor.execute(f"UPDATE notas SET data_saida = '', usuario = '' WHERE NFe = '{nota}'"                               )

                self.connection.commit()

        except AttributeError:
            print('faça a conexão para alterar campos.')


if __name__ == "__main__":
  db = DataBase()
  db.conecta()
  db.create_table_users()
  db.create_table_nfe()
  '''db.insert_user("teste", "teste390", "321", "usuario")'''
  '''teste = db.check_user('bryan390', '123')  print(teste)'''
  '''db.login_user("bryan390", "123")'''
  db.insert_data()
  db.close_connection()