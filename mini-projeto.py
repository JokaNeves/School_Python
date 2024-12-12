import random

def jogo_do_papel():
    print("Bem-vindo ao jogo Pedra, Papel ou Tesoura!")

    while True:
        try:
            rodadas = int(input("Insira o número de rodadas: "))
            if rodadas <= 0:
                print("Por favor, insira um número maior que 0.")
                continue
            break  
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    placar_jogador = 0
    placar_computador = 0
    empates = 0

    for i in range(1, rodadas + 1):
        print(f"\nRodada {i} de {rodadas}")

        while True:
            try:
                print("Qual é a sua jogada? \n Pedra -> 1 \n Papel -> 2 \n Tesoura -> 3")
                jogada = int(input("Escolha entre 1, 2 ou 3: "))
                if jogada not in [1, 2, 3]:
                    print("Escolha inválida. Tente novamente.")
                    continue
                break 
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")

        jogada_computador = random.randint(1, 3)

        if jogada == jogada_computador:
            print("Empate!")
            empates += 1
        elif (jogada == 1 and jogada_computador == 3) or \
             (jogada == 2 and jogada_computador == 1) or \
             (jogada == 3 and jogada_computador == 2):
            print("Bota!! Ganhaste")
            placar_jogador += 1
        else:
            print("Não tinhas chance! WIN PC!!!")
            placar_computador += 1

        jogadas = ["Pedra", "Papel", "Tesoura"]
        print(f"Você escolheu: {jogadas[jogada - 1]}")
        print(f"O computador escolheu: {jogadas[jogada_computador - 1]}")

    print("\nResultado Final:")
    print(f"Vitórias do jogador: {placar_jogador}")
    print(f"Vitórias do computador: {placar_computador}")
    print(f"Empates: {empates}")

    if placar_jogador > placar_computador:
        print("Parabéns! Você venceu o jogo!")
    elif placar_jogador < placar_computador:
        print("Que pena! O computador venceu o jogo!")
    else:
        print("O jogo terminou empatado!")

jogo_do_papel()
