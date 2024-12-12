# Jogo da Forca baseado nos exercícios

def exibir_palavra(palavra, letras_acertadas):
    palavra_exibida = ""
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    return palavra_exibida

def contar_espacos(frase):
    contador = 0
    for caractere in frase:
        if caractere == " ":
            contador += 1
    return contador

def jogo_da_forca():
    # Coletar a palavra e o número de tentativas do jogador 1
    palavra = input("Qual a palavra: ")
    tentativas_erradas_max = int(input("Quantas tentativas: "))

    letras_acertadas = ""
    letras_erradas = ""
    tentativas_erradas = 0

    while tentativas_erradas < tentativas_erradas_max:
        print("Palavra:", exibir_palavra(palavra, letras_acertadas))
        print("Erros (", tentativas_erradas, "/", tentativas_erradas_max, "): ", letras_erradas)
        
        letra = input("Qual a letra? ->  ")

        if len(letra) != 1:
            print("Insira apenas uma letra.")
            continue

        if letra in letras_acertadas or letra in letras_erradas:
            print("Já escolheste, tenta outra")
            continue

        if letra in palavra:
            letras_acertadas += letra
            print("Parabéns! Acertaste em cheio!!!")
        else:
            letras_erradas += letra + " "
            tentativas_erradas += 1
            print("Ops! Essa nao esta incluída =/")

        palavra_atual = ""
        for l in palavra:
            if l in letras_acertadas:
                palavra_atual += l
            else:
                palavra_atual += "_"

        if palavra_atual == palavra:
            print(f"Parabéns! Você acertou a palavra🥳: {palavra}")
            break

    else:
        print("Fim de Jogo!")
        print(f"Você errou {tentativas_erradas} vezes.")
        print(f"A palavra era: {palavra}")

jogo_da_forca()
