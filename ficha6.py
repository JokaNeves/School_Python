#Ex1
#import random
#num1 = random.randint(0, 9)
#num2 = random.randint(1, 9)
#num3 = random.uniform(0, 1)

#print("Nº aleatório entre 0 e 9:", num1)
#print("Nº aleatório entre 1 e 9:", num2)
#print("Nº aleatório entre 0 e 1:", num3)

#Ex2
#import random
#num= random.randint(0,6)
#print("Nº aleatório entre 0 e 6:", num)

#Ex3
#import random
#num=(random.randint(0,6))
#print("O nº saído apos o lançamento do dado foi:", num)

#Ex4
#import random
#resposta=input ("Lançar Dado: (S/N)?")

#while resposta=="S":
#    num=random.randint(1,6)
#    print( "Dado lançado!")
#    print("O nº saído após lançamento do dado foi:", num)
#    resposta=input("Lançar dado (S/N)?")
#print("Programa terminado!")
#
#Ex5
#import random

#while True:
#    a = input("Quantos dados (1, 2, 's' para sair)? ")
#    if a == 's': 
#        print("Terminado.")
#        break
#    if a not in ('1', '2'):  
#        print("Opção inválida! Digite 1, 2 ou 's' para sair.")
#        continue
#    
#    num_dados = int(a)
#    if num_dados == 1:
#        num = random.randint(1, 6)
#        print("Resultado:" ,num ,)
#    elif num_dados == 2:
#        num1 = random.randint(1, 6)
#        num2 = random.randint(1, 6)
#        total = num1 + num2
#        print("Dados:" ,num1 , "e" ,num2 , "-> Total =" ,total ,)

#Ex6
#randint(a, b):
#Faz aleatóriamente um número inteiro entre a e b, podendo ser ambos
#Ex:
#import random
#print(random.randint(1, 5))  #1, 2, 3, 4 ou 5
#randrange(start, stop( step) ):
#Gera um número inteiro aleatório entre start e stop, menos o stop. Também se pode usar o step para definir o intervalo entre os números.
#Ex:
#import random
#print(random.randrange(1, 5))  #1, 2, 3 ou 4
#print(random.randrange(1, 10, 2))  #1, 3, 5, 7 ou 9

#Ex7
#import random 
#numl = random.randint(1, 50) 
#num2 = random.randint(1, 50) 
#num3 = random.randint(1, 50) 
#num4 = random.randint(1, 50) 
#num5 = random.randint(1, 50) 
#estrelal = random.randint(1, 11) 
#estrela2 = random.randint(1, 11) 
#print("A chave do euromilhões é:", num1, num2, num3, num4, num5, "e estrelas: ", estrelal, estrela2)

#Ex8
#import random
#num = random.randint(1, 10)
#print("Adivinha o número oculto entre 1 e 10!")
#while True:
#    a = int(input("Qual é o teu palpite? "))
#    if a == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        print("Erraste. Tenta novamente!")

#Ex9
#import random
#num = random.randint(1, 10)
#print("Adivinha o número oculto entre 1 e 10!")
#tent = 3
#while tent > 0:
#    a = int(input("Qual é o teu palpite? "))
#    if a == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        tent -= 1
#        if tent > 0:
#            print("Erraste. Tens" , tent , "tentativa(s) restante(s).")
#        else:
#            print("Que pena! Não foi desta. Tenta outra vez!")
            
#Ex10
#import random
#i = int(input("Qual é o número inicial do intervalo? "))
#f = int(input("Qual é o número final do intervalo? "))
#tent = int(input("Quantas tentativas tens? "))
#num= random.randint(i, f)
#print(f"Adivinha o número oculto entre" ,i , "e" ,f,"!")
#while tent > 0:
#    a = int(input("Qual é o teu palpite? "))
#    if a == num:
#        print("PARABÉNS!! Acertaste no número!")
#        break
#    else:
#        tent -= 1
#        if tent> 0:
#            print("Erraste. Tens" ,tent , "tentativa(s) restante(s).")
#        else:
#            print("Que pena! Não foi desta. Tenta outra vez!")
            
#Ex11
#import random
#i = int(input("Qual é o número inicial do intervalo? "))
#f = int(input("Qual é o número final do intervalo? "))
#tent = int(input("Quantas tentativas tens? "))
#num = random.randint(i, f)
#print("Adivinha o número oculto entre" ,i , "e" ,f , "!")
#while tent > 0:
#    try:
#        a = int(input("Qual é o teu palpite? "))
#        if a < i or a > f:
#            print("O número introduzido é inválido! Deve estar entre" ,i , "e" ,f ,".")
#            continue
#        if a == num:
#            print("PARABÉNS!!! Acertaste no número.")
#            break
#        else:
#            tent -= 1
#            if tent > 0:
#                print("Erraste. Tens" ,tent , "tentativa(s) restante(s).")
#            else:
#                print("Que pena! Não foi desta. Tenta outra vez!")
#    except ValueError:
#        print("Entrada inválida! Introduz número inteiro.")

#Ex 12

import random

def mini_batalha_naval():
    print("Bem-vindo ao Mini-Batalha-Naval!")

    largura = int(input("Digite a dimensão horizontal do tabuleiro: "))
    altura = int(input("Digite a dimensão vertical do tabuleiro: "))

    barco_x = random.randint(1, largura)
    barco_y = random.randint(1, altura)

    tentativas = 0

    print("O barco esta pronto! Comece a jogar.")

    while True:
        tentativas += 1

        tentativa_x = int(input(f"posição em X #{tentativas}: "))
        tentativa_y = int(input(f"posição em y #{tentativas}: "))

        
        if tentativa_x == barco_x and tentativa_y == barco_y:
            print(f"PARABÉNS!!! Você acertou na {tentativas}ª tentativa!")
            break
        else:
            # Fornecer dicas de direção
            dicas = []

            if tentativa_x < barco_x:
                dicas.append("Leste")
            elif tentativa_x > barco_x:
                dicas.append("Oeste")

            if tentativa_y < barco_y:
                dicas.append("Norte")
            elif tentativa_y > barco_y:
                dicas.append("Sul")

            print(f"Água! Tente para {' e '.join(dicas)}.")

# Executar o jogo
mini_batalha_naval()







