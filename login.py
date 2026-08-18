import mysql.connector
import os
import time
from SQLxPython import *
from cadastros import *

def fazerLogin():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------LOGIN--------")
        print("1 - Já tenho uma conta")
        print("2 - Criar uma conta")
        escolha = input("")

        if escolha == "1":
            user = input("\nDigite seu usuário: ")
            senha = input("\nDigite sua senha: ")

            conn = conectar()
            cursor = conn.cursor(dictionary=True)

            try:
                sql = "SELECT id_user, nome, senha, pontuacao FROM usuarios WHERE nome = %s AND senha = %s"
                cursor.execute(sql, (user,senha))
                usuario = cursor.fetchone()

                if usuario:
                    print(f"Login realizado, bem vindo {usuario['nome']}")
                    time.sleep(3)
                    return usuario
                else:
                    print("Usuário ou senha incorreto(s)")
                    time.sleep(3)
            except Error as e:
                print(f"Erro no banco: {e}")
                time.sleep(5)
                return
            finally:
                cursor.close()
                conn.close()

        elif escolha == "2":
            cadastrarUser()
        else:
            print("Opção inválida")
            time.sleep(2)

fazerLogin()