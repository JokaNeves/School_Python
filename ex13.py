#Ex 13

import random

def mini_batalha_naval():
    print("Bem-vindo ao Mini-Batalha-Naval!")

    largura = int(input("Digite a dimensão em X do tabuleiro: "))
    comprimento = int(input("Digite a dimensão em Y do tabuleiro: "))
    altura = int(input("Digite a dimensão em Z do tabuleiro: "))
   
    barco_x = random.randint(1, largura)
    barco_y = random.randint(1, comprimento)
    barco_z = random.randint(1, altura)
   
    tentativas = 0

    print("O barco esta pronto! Comece a jogar.")

    while True:
        tentativas += 1

        tentativa_x = int(input(f"posição em X #{tentativas}: "))
        tentativa_y = int(input(f"posição em y #{tentativas}: "))
        tentativa_z = int(input(f"posição em z #{tentativas}: "))
        
        if tentativa_x == barco_x and tentativa_y == barco_y and tentativa_z == barco_z:
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
            
            if tentativa_z < barco_z:
                dicas.append("Sobe para cima!")
            elif tentativa_z > barco_z:
                dicas.append("Desce para baixo!")
            print(f"Água! Tente para {' e '.join(dicas)}.")

# Executar o jogo
mini_batalha_naval()