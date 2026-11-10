import mysql.connector
from mysql.connector import Error

CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "03141116*Die",
    "database" : "biblioteca",
}

def conectar():
    try:
        return mysql.connector.connect(**CONFIG)
    except Error as erro:
        print(f"Erro ao conectaro ao MySQL: {erro}")
        raise

if __name__ == "__main__":
    con = conectar()
    print("Conectado ao MySQL versão: ", con.get_server_info())
    con.close()