from SQLxPython import *
from login_menu import *

def level1(usuario):
    pontos = usuario['pontuacao']
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem vindo ao ReciclaQuiz! O jogo é simples, 3 chances para acertar 5 perguntas sobre reciclagem e sustentabilidade. Boa sorte!")
    time.sleep(5)
    print("level 1:")
    time.sleep(1.5)
    chances = 3 
    print(f"Chances restantes: {chances}")
    time.sleep(3)
    while True:
       

    
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 1-1 - Quantas lixeiras recicláveis existem?")
            print("a) 4 cores principais (Papel, Plástico, Vidro, Metal)")
            print("b) 10 cores padrão de coleta seletiva (incluindo orgânico, hospitalar, perigoso, etc.)")
            print("c) 2 cores apenas")
            resposta1_1 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_1 == "b":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta1_1 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
            

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 1-2 - Qual energia vem do Sol?")
            print("a) Energia Eólica")
            print("b) Energia Solar")
            print("c) Energia Geotérmica")
            resposta1_2 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_2 == "b":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta1_2 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
           

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 1-3 - Qual energia vem do vento?")
            print("a) Energia Eólica")
            print("b) Energia Hídrica")
            print("c) Energia Solar")
            resposta1_3 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_3 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(1)
                break
            elif resposta1_3 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando1 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando1, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 1-4 - O que podemos plantar para ajudar o ambiente?")
            print("a) Plantas exóticas invasoras")
            print("b) Árvores nativas e plantas melíferas (que atraem abelhas)")
            print("c) Apenas grama sintética")
            resposta1_4 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_4 == "b":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta1_4 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando2 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando2, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 1-5 - Qual cor da lixeira representa papel?")
            print("a) Amarelo")
            print("b) Verde")
            print("c) Azul")
            resposta1_5 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_5 == "c":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta1_5 in ["a", "b"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando3 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando3, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        sql = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
        cursor.execute(sql, (pontos, usuario['id_user']))
        conn.commit()
        print(f"Fim do Level 1! Chances restantes: {chances} | Pontuação final: {pontos}")
        time.sleep(5)
        
        return pontos







def level2(usuario):
    pontos = usuario['pontuacao']
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Esse é o level 2, mais complicado que o 1. Você continua tendo 3 chances, boa sorte.")
    time.sleep(5)
    print("level 2:")
    time.sleep(1.2)
    chances = 3 
    print(f"Chances restantes: {chances}")
    time.sleep(3)
    while True:
       

    
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 2-1 - Qual desses materiais são reciclaveis?")
            print("a) Garrafa de vidro")
            print("b) Papel higiênico usado")
            print("c) Guardanapo sujo de comida")
            resposta2_1 = input("Qual é a resposta correta? ").strip().lower()
            if resposta2_1 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta2_1 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
            

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 2-2 - O que devemos fazer com uma garrafa PET antes de encaminhá-la para reciclagem?")
            print("a) Queimar")
            print("b) Esvaziá-la e, se possível, compactá-la")
            print("c) Jogá-la com restos de comida")
            resposta2_2 = input("Qual é a resposta correta? ").strip().lower()
            if resposta2_2 == "b":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta2_2 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
           

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 2-3 - Por que separar corretamente os resíduos é importante?")
            print("a) Para facilitar a reciclagem e diminuir a quantidade de lixo descartado")
            print("b) Para produzir mais lixo")
            print("c) Para aumentar a poluição")
            resposta2_3 = input("Qual é a resposta correta? ").strip().lower()
            if resposta2_3 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(1)
                break
            elif resposta2_3 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando1 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando1, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 2-4 - O que é coleta seletiva?")
            print("a) Separar o lixo de acordo com o seu tipo")
            print("b) Coleta de todos os resíduos misturados")
            print("c) Coleta de resíduos perigosos")
            resposta2_4 = input("Qual é a resposta correta? ").strip().lower()
            if resposta2_4 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta2_4 in ["b", "c"]:
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando2 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando2, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 2-5 - O que devemos fazer com pilhas e baterias usadas?")
            print("a) Jogar na privada")
            print("b) Jogá-las no lixo comum")
            print("c) Entregá-las em pontos de coleta apropriados")
            resposta2_5 = input("Qual é a resposta correta? ").strip().lower()
            if resposta2_5 == "c":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta2_5 in ["a", "b"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando3 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando3, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        sql = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
        cursor.execute(sql, (pontos, usuario['id_user']))
        conn.commit()
        print(f"Fim do Level 2! Chances restantes: {chances} | Pontuação final: {pontos}")
        time.sleep(5)
        
        return pontos

def level3(usuario):
    pontos = usuario['pontuacao']
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Esse é o level 3, o mais complicado de todos. 3 chances, boa sorte.")
    time.sleep(5)
    print("level 3:")
    time.sleep(1.4)
    chances = 3 
    print(f"Chances restantes: {chances}")
    time.sleep(3)
    while True:
       

    
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 3-1 - Qual dos três princípios abaixo representa a ordem mais conhecida dos 3 Rs?")
            print("a) Reclamar, reutilizar, reciclar")
            print("b) Reduzir, Rasgar e recitar")
            print("c) Reduzir, reutilizar e reciclar")
            resposta3_1 = input("Qual é a resposta correta? ").strip().lower()
            if resposta3_1 == "c":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(1.8)
                break
            elif resposta3_1 in ["a", "b"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
            

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 3-2 - Qual destes materiais pode ser reciclado várias vezes sem perder suas características básicas?")
            print("a) Vidro")
            print("b) Papelão")
            print("c) Papel")
            resposta3_2 = input("Qual é a resposta correta? ").strip().lower()
            if resposta3_2 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta3_2 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue
           

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 3-3 -  Qual destes materiais demora muito tempo para se decompor na natureza?")
            print("a) Plastico")
            print("b) Papel")
            print("c) Casca de banana")
            resposta3_3 = input("Qual é a resposta correta? ").strip().lower()
            if resposta3_3 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(1)
                break
            elif resposta3_3 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando1 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando1, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 3-4 - Qual atitude ajuda a diminuir a quantidade de lixo produzida?")
            print("a) Usar lixo/objetos descartáveis quando possível")
            print("b) Reutilizar objetos e evitar desperdícios")
            print("c) Jogar materiais recicláveis no lixo comum")
            resposta3_4 = input("Qual é a resposta correta? ").strip().lower()
            if resposta3_4 == "b":
                pontos += 1
                print("Resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta3_4 in ["a", "c"]:
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando2 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando2, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("Escolha uma opção válida\n")
                time.sleep(1)
                continue

        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pergunta 3-5 - O que é “downcycling”?")
            print("a) Transformar um material em um produto de qualidade ou valor funcional inferior ao original")
            print("b) Transformar qualquer resíduo em combustível")
            print("c) Reutilizar um produto sem nenhuma alteração")
            resposta3_5 = input("Qual é a resposta correta? ").strip().lower()
            if resposta3_5 == "a":
                pontos += 1
                print("resposta certa\n")
                print(f"Pontuação atual: {pontos}")
                time.sleep(2)
                break
            elif resposta3_5 in ["b", "c"]:
                print("Resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                time.sleep(2)
                break
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")
                    time.sleep(5)
                    comando3 = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
                    cursor.execute(comando3, (pontos, usuario['id_user']))
                    conn.commit()

                    cursor.close()
                    conn.close()

                    return pontos
                break
            else:
                print("Escolha uma opção válida\n")
                time.sleep(1)
                continue

        sql = "UPDATE usuarios SET pontuacao = %s WHERE id_user = %s"
        cursor.execute(sql, (pontos, usuario['id_user']))
        conn.commit()
        print(f"Você zerou todos os niveis! Chances de sobra: {chances} | Pontuação final: {pontos}")
        time.sleep(5)
        
        return pontos