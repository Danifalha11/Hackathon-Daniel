from SQLxPython import *
import time
import string

def validarUser(user, senha):
    if user.strip() == "":
        print("Campo vazio em Nome")
        time.sleep(3)
        return False

    if len(user) > 25:
        print("Nome muito longo")
        time.sleep(3)
        return False
    
    if len(user) < 3:
        print("Nome muito pequeno")
        time.sleep(3)
        return False

    if senha.strip() == "":
        print("Campo vazio em Senha")
        time.sleep(3)
        return False

    if len(senha) < 8:
        print("Senha muito pequena")
        time.sleep(3)
        return False

    temNum = any(char.isdigit() for char in senha)
    caracteresEspeciais = string.punctuation
    temEspecial = any(char in caracteresEspeciais for char in senha)

    if not temNum or not temEspecial:
        print("Senha deve conter pelo menos um número/caractere especial")
        time.sleep(5)
        return False

    return True

def validarNome(nome):
    if nome.strip() == "":
        print("Campo vazio em Nome")
        time.sleep(3)
        return False

    if len(nome) > 25:
        print("Nome muito longo")
        time.sleep(3)
        return False
    
    if len(nome) < 3:
        print("Nome muito pequeno")
        time.sleep(3)
        return False

    return True

def validarSenha(senha):
    if senha.strip() == "":
        print("Campo vazio em Senha")
        time.sleep(3)
        return False

    if len(senha) < 8:
        print("Senha muito pequena")
        time.sleep(3)
        return False

    temNum = any(char.isdigit() for char in senha)
    caracteresEspeciais = string.punctuation
    temEspecial = any(char in caracteresEspeciais for char in senha)

    if not temNum or not temEspecial:
        print("Senha deve conter pelo menos um número/caractere especial")
        time.sleep(5)
        return False

    return True