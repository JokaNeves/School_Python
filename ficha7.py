#Exercício1
#a=(input("Escreve uma frase:"))
#print( len(a) )

#Exercício2
#a=(input("Escreve uma frase:"))

#frase = ""

#for l in s:
#    if l == " ":
#        frase += "_"
#    else:
#        frase += l

#print(frase)

#Exercício3
#a=(input("Escreve uma frase:"))

#for i in range(len(a)-1, -1, -1):
#     print(a[i], end="")

#Exercício4
#a=(input("Escreve uma frase:"))

#contador_E = 0
#contador_L = 0

#for l in a:
#    if l == " ":
#        contador_E += 1
#    else:
#        contador_L += 0

#print("O número de espaços nesta frase é", contador_E)

#Exercício5
#a=(input("Escreve uma frase:"))

#if a[-1] == ".":
#    print("A frase apresentada acaba com ponto final.")
#else:
#    print("A frase apresentada não acaba em ponto final.")

#Exercício6
#a=(input("Escreve um nome:"))

#if s[-1] == "a":
#    print("Provavelmente é uma rapariga.")
#else:
#    print("Provavelmente é um rapaz.")

#Exercício7
#s=(input("Escreve uma frase:"))

#if s[-1] == "!":
#    print("A frase apresentada é exclamativa.")
#elif s[-1] == "?":
#    print("A frase apresentada é interrogativa.")
#else:
#    print("A frase apresentada é afirmativa.")

#Exercício8
#s=(input("Escreve uma frase:"))

#if s[-1] == "!":
#    print("A frase apresentada é exclamativa.")
#elif s[-1] == "?":
#    print("A frase apresentada é interrogativa.")
#elif s[-1] == "?" and s[-2] == "!":
#    print("A frase apresentada é interrogativa exclamativa.")
#elif s[-1] == "!" and s[-2] == "?":
#print("A frase apresentada é interrogativa exclamativa.")
#else:
#    print("A frase apresentada é afirmativa.")

#Exercício9

#Atendendo ao formato normal do zoom do terminal, o número de caracteres que se pode escrever em cada linha da consola
#pode ser determinado por:

#a=input()
#print(len(a))

#Assim sendo estes que foi-me aparecdio no terminal
#O número de caracteres é 287.


#Exercício10
#a=(input("Escreve um frase:"))

#largura_terminal=149
#espacos = largura_terminal - len(a)

#if espacos > 0:
#    print(" " * espacos + a)
#else:
#    print(a)