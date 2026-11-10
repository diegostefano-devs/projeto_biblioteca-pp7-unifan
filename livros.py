from conexao import conectar

def cadastrar_livros(titulo, autor, ano=None, isbn=None):
    con = conectar()
    sql = "INSERT INTO biblioteca VALUES (%s, %s, %s, %s, %S)"
    try:
        cursor = con.cursor()
        cursor.execute(sql, (titulo, autor, ano, isbn))
        con.commit()
        return cursor.lastrowid
    finally:
        con.close()

def listar_livros():
    con = conectar()
    try:
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM livros ORDER BY titulo")
        return cursor.fetchall()
    finally:
        con.close()

def buscar_livro(termo):
    sql = "SELECT * FROM livros WHERE titulo LIKE %s OR autor LIKE %s"
    padrao = f"%{termo}%"
    con = conectar()
    try:
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql, {padrao, padrao})
        return cursor.fetchall()
    finally:
        con.close()

def buscar_id_livro(id_livro):
    con = conectar()
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM livros WHERE id = %s", (id_livro))
        return cursor.fetchone()
    finally:
        cursor.close()
def atualizar_livro(id_livro, titulo, autor, ano, isbn, disponivel):
    con = conectar()
    sql = """UPDATE livros SET titulo = %s, autor = %s, ano = %s, isbn = %s, disponivel = %s WHERE id = %s"""
    try:
        cursor = con.cursor()
        cursor.execute(sql, (titulo, autor, ano, isbn, disponivel, id_livro))
        con.commit()
        return cursor.rowcount > 0
    finally:
        con.close