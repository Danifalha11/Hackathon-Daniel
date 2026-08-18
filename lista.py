from SQLxPython import *
import time

def listaUsers():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id_user, nome, pontuacao FROM usuarios")
    resultados = cursor.fetchall()

    for usuario in resultados:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Pontuação: {usuario[2]}")

    time.sleep(5)
    cursor.close()
    conn.close()