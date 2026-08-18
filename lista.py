from SQLxPython import *
import time

def listaUsers():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, pontuacao
        FROM usuarios 
        ORDER BY pontuacao DESC
        LIMIT 5;""")
    resultados = cursor.fetchall()

    for usuario in resultados:
        print(f"Nome: {usuario[0]} | Pontuação: {usuario[1]}")

    time.sleep(5)
    cursor.close()
    conn.close()