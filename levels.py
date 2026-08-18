def level1():
    print("level 1:")
    chances = 3 
    print(f"Chances restantes: {chances}")
    while True:
       

    
        while True:
            print("Pergunta 1 - Quantas lixeiras recicláveis existem?")
            print("a) 4 cores principais (Papel, Plástico, Vidro, Metal)")
            print("b) 10 cores padrão de coleta seletiva (incluindo orgânico, hospitalar, perigoso, etc.)")
            print("c) 2 cores apenas")
            resposta1_1 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_1 == "b":
                print("resposta certa\n")
                print(f"Chances restantes: {chances}")
                break
            elif resposta1_1 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue
            

        
        while True:
            print("Pergunta 2 - Qual energia vem do Sol?")
            print("a) Energia Eólica")
            print("b) Energia Solar")
            print("c) Energia Geotérmica")
            resposta1_2 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_2 == "b":
                print("resposta certa\n")
                print(f"Chances restantes: {chances}")
                break
            elif resposta1_2 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 3 - Qual energia vem do vento?")
            print("a) Energia Eólica")
            print("b) Energia Hídrica")
            print("c) Energia Solar")
            resposta1_3 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_3 == "a":
                print("resposta certa\n")
                print(f"Chances restantes: {chances}")
                break
            elif resposta1_3 in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")   
                    return
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 4 - O que podemos plantar para ajudar o ambiente?")
            print("a) Plantas exóticas invasoras")
            print("b) Árvores nativas e plantas melíferas (que atraem abelhas)")
            print("c) Apenas grama sintética")
            resposta1_4 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_4 == "b":
                print("resposta certa\n")
                print(f"Chances restantes: {chances}")
                break
            elif resposta1_4 in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")   
                    return
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 5 - Qual cor da lixeira representa papel?")
            print("a) Amarelo")
            print("b) Verde")
            print("c) Azul")
            resposta1_5 = input("qual é a resposta correta? ").strip().lower()
            if resposta1_5 == "c":
                print("resposta certa\n")
                print(f"Chances restantes: {chances}")
                break
            elif resposta1_5 in ["a", "b"]:
                print("resposta errada\n")
                chances -= 1
                
                if chances == 0:
                    print("Você perdeu todas as chances! Game Over.")   
                    return
                break
            else:
                print("escolha uma opção válida\n")
                continue

        print(f"Fim do Level 1! Chances restantes: {chances}")
        break
    
level1()