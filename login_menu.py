import mysql.connector
import os
import time
from SQLxPython import *
from cadastros import *
from atualizar import *
from deletar import *
from levels import *
from lista import *

def fazerLogin():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------LOGIN--------")
        print("1 - Já tenho uma conta")
        print("2 - Criar uma conta")
        escolha = input()

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
                    print(f"Login realizado com sucesso!")
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


def menuUser(usuario):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"------BEM VINDO {usuario['nome']}!------")
        print("----O QUE VOCÊ DESEJA FAZER?------")
        print("\n1 - ReciclaQuiz")
        print("2 - Ver perfil")
        print("3 - Ver classificação")
        print("4 - Atualizar perfil")
        print("5 - Deletar perfil")
        print("6 - Sair")
        opcao = input()
        
        if opcao == "1":
            print("Iniciando o ReciclaQuiz...")
            time.sleep(2)
            print("Temos 3 niveis disponiveis:")
            time.sleep(1)
            print("1 - Fácil")
            time.sleep(1)
            print("2 - Médio")
            time.sleep(1)
            print("3 - Difícil")
            time.sleep(2)
            escolha_level = input("Escolha o nível que deseja jogar: ")
            if escolha_level == "1":
                usuario['pontuacao'] = level1(usuario)
            elif escolha_level == "2":
                if usuario['pontuacao'] >= 5:
                    usuario['pontuacao'] = level2(usuario)
                else:
                    print("Tenha pelo menos 5 pontos para jogar o nível 2")
                    time.sleep(2)
            elif escolha_level == "3":
                if usuario['pontuacao'] >= 10:
                    usuario['pontuacao'] = level3(usuario)
                else:
                    print("Tenha pelo menos 10 pontos para jogar o nível 3")
                    time.sleep(2)
        elif opcao == "2":
            print(f"ID: {usuario['id_user']} | Usuário: {usuario['nome']} | Pontuação: {usuario['pontuacao']}")
            input("Precione Enter para voltar")
        elif opcao == "3":
            listaUsers()
        elif opcao == "4":
            atualizarUser(id_user=usuario['id_user'])
        elif opcao == "5":
            deletarUsuario(id_user=usuario['id_user'])
            break
        elif opcao == "6":
            print("Saindo...")
            time.sleep(2)
            break
      