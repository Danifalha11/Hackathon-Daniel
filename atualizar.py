import time
from SQLxPython import *
from validacao import *

def atualizarUser(id_user):
    confirmacao = input("Tem certeza que deseja atualizar sua conta? (S/N): ").upper()

    if confirmacao == 'S':
        conn = conectar()
        cursor = conn.cursor()

        try:
            novo_nome = input("Digite o novo nome de usuário (vazio para não alterar): ")
            nova_senha = input("Digite a nova senha (vazio para não alterar): ")

            if novo_nome and nova_senha:
                if validarUser(novo_nome, nova_senha):
                    sql = "UPDATE usuarios SET nome = %s, senha = %s WHERE id_user = %s"
                    cursor.execute(sql, (novo_nome, nova_senha, id_user))
                else:
                    print("Nome de usuário ou senha inválidos. Nenhum dado foi alterado.")
                    time.sleep(2)
                    return
            elif novo_nome:
                if validarNome(novo_nome):
                    sql = "UPDATE usuarios SET nome = %s WHERE id_user = %s"
                    cursor.execute(sql, (novo_nome, id_user))
                else:
                    print("Nome de usuário inválido. Nenhum dado foi alterado.")
                    time.sleep(2)
                    return
            elif nova_senha:
                if validarSenha(nova_senha):
                    sql = "UPDATE usuarios SET senha = %s WHERE id_user = %s"
                    cursor.execute(sql, (nova_senha, id_user))
                else:
                    print("Senha inválida. Nenhum dado foi alterado.")
                    time.sleep(2)
                    return
            else:
                print("Operação cancelada. Nenhum dado foi alterado.")
                time.sleep(2)
                return

            conn.commit()
            print("Conta atualizada com sucesso!")
            time.sleep(2)
            
        except Error as e:
            print(f"\nErro ao atualizar conta: {e}")
            time.sleep(3)
            return False
        finally:
            cursor.close()
            conn.close()