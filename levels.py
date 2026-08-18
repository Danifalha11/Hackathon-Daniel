pontos = 0
chances = 3
def levels():
    
    def level1():
        global chances, pontos
        print("level 1:")
        
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
                    pontos += 1
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
                    pontos += 1
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
                    pontos += 1
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
                    pontos += 1
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
                    pontos += 1
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
        

    def level2():
        global chances, pontos
        print("Level 2: ")
        print("você recuperou 3 chances")
        chances += 3 
        print(f"Chances restantes: {chances}")
        while True:
            print("level 2:")
            chances = 3 
            print(f"Chances restantes: {chances}")
    
        
            while True:
                print("Pergunta 1 - Qual destes materiais NÃO pode ser reciclado na lixeira de plástico/papel devido à contaminação ou composição?")
                print("a) Embalagens Longa Vida (Tetra Pak)")
                print("b) Papel térmico de cupom fiscal e fita adesiva")
                print("c) Garrafas PET transparentes e tampas de polipropileno")
                resposta2_1 = input("qual é a resposta correta? ").strip().lower()
                if resposta2_1 == "b":
                    print("resposta certa\n")
                    pontos += 1
                    print(f"Chances restantes: {chances}")
                    break
                elif resposta2_1 in ["a", "c"]:
                    print("resposta errada\n")
                    chances -= 1
                    print(f"Chances restantes: {chances}")
                    break
                else:
                    print("escolha uma opção válida\n")
                    continue

            
            while True:
                print("Pergunta 2 - O que deve ser feito com uma caixa de pizza engordurada antes do descarte?")
                print("a) Lavar com água e detergente neutro para retirar toda a gordura do papel")
                print("b) Rasgar e descartar a parte limpa no papel e a parte engordurada no lixo comum/orgânico")
                print("c) Descartar inteira no papelão, pois a gordura evapora no processo de reciclagem")
                resposta2_2 = input("qual é a resposta correta? ").strip().lower()
                if resposta2_2 == "b":
                    print("resposta certa\n")
                    pontos += 1
                    print(f"Chances restantes: {chances}")
                    break
                elif resposta2_2 in ["a", "c"]:
                    print("resposta errada\n")
                    chances -= 1
                    print(f"Chances restantes: {chances}")
                    break
                else:
                    print("escolha uma opção válida\n")
                    continue

            
            while True:
                print("Pergunta 3 - Qual o descarte correto para espelhos, lâmpadas e vidros pyrex (refratários)?")
                print("a) Lixeira verde (vidro), pois todos possuem a mesma base de sílica")
                print("b) Lixeira cinza (não reciclável) ou pontos específicos de logística reversa")
                print("c) Lixeira amarela (metal), devido à camada reflexiva de alumínio/prata")
                resposta2_3 = input("qual é a resposta correta? ").strip().lower()
                if resposta2_3 == "b":
                    print("resposta certa\n")
                    pontos += 1
                    print(f"Chances restantes: {chances}")
                    break
                elif resposta2_3 in ["a", "c"]:
                    print("resposta errada\n")
                    chances -= 1
                    print(f"Chances restantes: {chances}")
                    break
                else:
                    print("escolha uma opção válida\n")
                    continue

            
            while True:
                print("Pergunta 4 - Por que o isopor (EPS) raramente é reciclado na prática, embora seja tecnicamente reciclável?")
                print("a) Porque é composto por 98% de ar, tornando o transporte e a triagem economicamente inviáveis")
                print("b) Porque libera gases altamente tóxicos assim que entra em contato com a água na lavagem")
                print("c) Porque derrete em temperaturas baixas demais, queimando os maquinários de extrusão")
                resposta2_4 = input("qual é a resposta correta? ").strip().lower()
                if resposta2_4 == "a":
                    print("resposta certa\n")
                    pontos += 1
                    print(f"Chances restantes: {chances}")
                    break
                elif resposta2_4 in ["b", "c"]:
                    print("resposta errada\n")
                    chances -= 1
                    print(f"Chances restantes: {chances}")
                    break
                else:
                    print("escolha uma opção válida\n")
                    continue

            
            while True:
                print("Pergunta 5 - O que é o processo de 'Upcycling' na gestão de resíduos?")
                print("a) A fragmentação mecânica do plástico em pellets de menor pureza para fazer sacos de lixo")
                print("b) O reaproveitamento de um resíduo criando um objeto de maior valor agregado ou utilidade sem passar por processo industrial pesado")
                print("c) A incineração controlada de resíduos sólidos para geração de energia elétrica em usinas")
                resposta2_5 = input("qual é a resposta correta? ").strip().lower()
                if resposta2_5 == "b":
                    print("resposta certa\n")
                    pontos += 1
                    print(f"Chances restantes: {chances}")
                    break
                elif resposta2_5 in ["a", "c"]:
                    print("resposta errada\n")
                    chances -= 1
                    print(f"Chances restantes: {chances}")
                    break
                else:
                    print("escolha uma opção válida\n")
                    continue

            print(f"Fim do Level 2! Chances restantes: {chances}")

    def level3():
        global chances, pontos
        print("Level 3: ")
        print("você recuperou 3 chances")
        chances += 3 
        print(f"Chances restantes: {chances}")
        
        
        while True:
            print("Pergunta 1 - Qual é o principal desafio técnico na reciclagem mecânica de embalagens plásticas multicamadas (ex.: Sachês com PE, PET e alumínio)?")
            print("a) A incompatibilidade termodinâmica e a diferença nos pontos de fusão dos polímeros envolvidos.")
            print("b) O excesso de umidade que impede a trituração dos materiais no moinho.")
            print("c) A alta condutividade elétrica do alumínio que queima os extrusores industriais.")
            resposta = input("qual é a resposta correta? ").strip().lower()
            if resposta == "a":
                print("resposta certa\n")
                pontos += 1
                print(f"Chances restantes: {chances}")
                break
            elif resposta in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 2 - No processo de reciclagem química de polímeros via Pirólise, qual é o principal resultado da transformação da matéria-prima?")
            print("a) A dissolução do plástico em solventes orgânicos sem alterar sua estrutura molecular.")
            print("b) A quebra térmica das cadeias macromoleculares na ausência de oxigênio, gerando frações de hidrocarbonetos (óleo e gás sintetizado).")
            print("c) A oxidação completa dos plásticos resultando exclusivamente em cinzas e água.")
            resposta = input("qual é a resposta correta? ").strip().lower()
            if resposta == "b":
                print("resposta certa\n")
                pontos += 1
                print(f"Chances restantes: {chances}")
                break
            elif resposta in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 3 - Na reciclagem do PET para uso em contato direto com alimentos (grade Food Contact / Bottle-to-Bottle), qual etapa é indispensável para elevar a viscosidade intrínseca do material?")
            print("a) Lavagem alcalina com soda cáustica a frio.")
            print("b) Cristalização e Polimerização no Estado Sólido (SSP - Solid State Polymerization).")
            print("c) Aglomeração mecânica sob alta pressão hidrostática.")
            resposta = input("qual é a resposta correta? ").strip().lower()
            if resposta == "b":
                print("resposta certa\n")
                pontos += 1
                print(f"Chances restantes: {chances}")
                break
            elif resposta in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 4 - Durante a triagem automatizada de resíduos sólidos em usinas de reciclagem, qual tecnologia é amplamente utilizada para a identificação e separação rápida de diferentes tipos de resina plástica?")
            print("a) Espectroscopia de Infravermelho Próximo (NIR - Near-Infrared).")
            print("b) Difração de Raios-X de Alta Intensidade (XRD).")
            print("c) Espectrometria de Massa por Plasma Indutivamente Acoplado (ICP-MS).")
            resposta = input("qual é a resposta correta? ").strip().lower()
            if resposta == "a":
                print("resposta certa\n")
                pontos += 1
                print(f"Chances restantes: {chances}")
                break
            elif resposta in ["b", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue

        
        while True:
            print("Pergunta 5 - Na reciclagem de baterias de íon-lítio (LIBs), qual é a principal diferença operacional entre os processos Hidrometalúrgico e Pirometalúrgico?")
            print("a) O processo hidrometalúrgico utiliza fusão em altas temperaturas, enquanto o pirometalúrgico utiliza compostos biológicos.")
            print("b) O processo hidrometalúrgico emprega lixiviação ácida/básica em meio aquoso para extrair metais, enquanto o pirometalúrgico usa fundição a altas temperaturas para separar a liga metálica.")
            print("c) O processo pirometalúrgico recupera 100% do eletrólito líquido, enquanto o hidrometalúrgico o descarta como resíduo gasoso.")
            resposta = input("qual é a resposta correta? ").strip().lower()
            if resposta == "b":
                print("resposta certa\n")
                pontos += 1
                print(f"Chances restantes: {chances}")
                break
            elif resposta in ["a", "c"]:
                print("resposta errada\n")
                chances -= 1
                print(f"Chances restantes: {chances}")
                break
            else:
                print("escolha uma opção válida\n")
                continue
    level1()
    if chances > 0:
        level2()
    if chances > 0:
        level3()
   
        
    
levels()