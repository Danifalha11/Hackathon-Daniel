from SQLxPython import *
from validacao import *
import time

def cadastrarUser():
    conn = conectar()
    cursor = conn.cursor()

    user = input("Digite o nome de usuário (mínimo 5 | máximo 25): ")
    senha = input("Digite sua senha (mínimo 8): ")

    sql = "INSERT INTO usuarios (nome, senha, pontuacao) VALUES (%s, %s, 0)"

    try:
        if validarUser(user,senha):
            cursor.execute(sql, (user,senha))
            conn.commit()
            print("Usuário cadastrado")
            time.sleep(3)
    except Error as e:
        print(f"Erro no cadastro: {e}")
        time.sleep(5)
        return
    finally:
        cursor.close()
        conn.close()
