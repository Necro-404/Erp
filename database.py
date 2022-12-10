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

#login usuário
  def login_user(self, user, password):
    try:
      cursor = self.connection.cursor()
      cursor.execute("SELECT * FROM users;")
      print(user, password)

      for linha in cursor.fetchall():
        if linha[2].upper() == user.upper() and linha[3] == password:
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
        if linha[2].upper() == user.upper() and linha[3] == password :
          return linha[4].upper()
        elif linha[2].upper() == user.upper() and linha[3] != password :
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

if __name__ == "__main__":
  db = DataBase()
  db.conecta()
  db.create_table_users()
  '''db.insert_user("teste", "teste390", "321", "usuario")'''
  '''teste = db.check_user('bryan390', '123')  print(teste)'''
  '''db.login_user("bryan390", "123")'''
  db.close_connection()