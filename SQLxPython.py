import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Senac2026",
)

cursor = conn.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS ReciclaQuiz;
""")

cursor.execute("USE ReciclaQuiz")

def conectar():
    try:
        conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "Senac2026",
            database = "ReciclaQuiz",
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id_user INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(25) NOT NULL UNIQUE,
        senha VARCHAR(50) NOT NULL,
        pontuacao INT
    )
""")

