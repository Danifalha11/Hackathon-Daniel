import mysql.connector
import os
from SQLxPython import *
from cadastros import *

def fazerLogin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------LOGIN------")
    print("1 - Já tenho uma conta")
    print("2 - Criar uma conta")
    escolha = input("")

    if escolha == "1":
        ...
    elif escolha == "2":
        cadastrarUser()
    else:
        print("Opção inválida")
        time.sleep(2)
        return

fazerLogin()