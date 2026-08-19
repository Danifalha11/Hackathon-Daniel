from SQLxPython import *
import time

def deletarUsuario(id_user):
    confirmacao = input("Tem certeza que deseja excluir sua conta? (S/N): ").upper()
    
    if confirmacao == 'S':
        conn = conectar()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM usuarios WHERE id_user = %s"
            cursor.execute(sql, (id_user,))
            conn.commit()  
            
            print("\nConta excluída com sucesso!")
            time.sleep(2)
            return True

        except Error as e:
            print(f"\nErro ao excluir conta: {e}")
            time.sleep(3)
            return False

        finally:
            cursor.close()
            conn.close()
    else:
        print("\nOperação cancelada.")
        time.sleep(1.5)
        return False