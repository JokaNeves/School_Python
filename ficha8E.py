
# Ficha de Trabalho 8

# --- Introdução ---

#1 Observa a função apresentada. O que faz esta função, e como poderá ser utilizada num programa?
# A função ola imprime "Olá mundo" na consola. Pode ser usada para dizer uma boas vindas ao utilizador ao iniciar o programa.

#2 Qual o resultado de um programa como o apresentado?
#Olá mundo
#Olá mundo
#Olá mundo

#3 Resultado com for:
#Olá mundo
#Olá mundo
#Olá mundo

#4 Função com argumento nome
# Resultado da chamada ola("Maria") é: Olá Maria

#5 Para este programa, qual será o resultado?
#Vai dar erro porque estás a chamar a função ola("Maria") antes dela ser definida. 
# Em Python, as funções têm de ser definidas primeiro.

# --- 1 ---
# a) Objetivo: Devolver o triplo de um número
# b) Nome da função: triplo
# c) Parâmetros: 1 (n)
# d) return: devolve o valor ao programa
# e) Cabeçalho: def triplo(n):
# f) Corpo:
#    t = 3 * n
#    return t
# g) triplo(5) -> 15
# h) triplo("PÃO") -> "PÃOPÃOPÃO"
def triplo(n):
    t = 3 * n
    return t

# --- 2 ---
def bom_dia():
    print("Bom dia")

bom_dia()

# --- 3 ---
def bom_dia():
    print("Bom dia")

def boa_tarde():
    print("Boa tarde")

def boa_noite():
    print("Boa noite")

hora = int(input("Que horas são? "))
if hora < 12:
    bom_dia()
elif hora < 20:
    boa_tarde()
else:
    boa_noite()

# --- 4 ---
def boas_vindas(hora):
    if hora < 12:
        print("Bom dia")
    elif hora < 20:
        print("Boa tarde")
    else:
        print("Boa noite")

hora = int(input("Que horas são? "))
boas_vindas(hora)

# --- 5 ---
# Resultado esperado:
# 1
# 5
# 1
# A variável n dentro da função é local, não afeta a n exterior.
def exemplo():
    n = 5
    print(n)

n = 1
print(n)
exemplo()
print(n)

# --- 6 ---
# Resultado esperado:
# 1
# 5
# 5
# A variável n foi modificada globalmente devido ao uso de "global"
def exemplo_global():
    global n
    n = 5
    print(n)

n = 1
print(n)
exemplo_global()
print(n)

# --- 7 ---
def dobro(n):
    return 2 * n

# --- 8 ---
def soma(a, b):
    return a + b

# --- 9 ---
def maior(a, b):
    return a if a > b else b

# --- 10 ---
def um_a_dez():
    for i in range(1, 11):
        print(i)

# --- 11 ---
def contar_ate(n):
    for i in range(1, n+1):
        print(i)

# --- 12 ---
def intervalo(a, b):
    for i in range(a, b+1):
        print(i)

# --- 13 ---
def media(n1, n2):
    return (n1 + n2) / 2

# --- 14 ---
def media_valida(n1, n2):
    if 0 <= n1 <= 20 and 0 <= n2 <= 20:
        return (n1 + n2) / 2
    return -1

# --- 15 ---
def aprovado(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media >= 10

# --- 16 ---
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# --- 17 ---
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# --- 18 ---
def termo(n):
    return (n + 1) / n

# --- 19 ---
# A função vizinhos devolve dois valores: anterior e seguinte ao número n.
# Diferença: retorna múltiplos valores.
def vizinhos(n):
    anterior = n - 1
    seguinte = n + 1
    return anterior, seguinte

# --- 20 ---
def metade_dobro(n):
    return n / 2, n * 2

# --- 21 ---
def area_perimetro(a, b):
    return a * b, 2 * (a + b)

# --- 22 ---
def divisoes(a, b):
    return a % b, a // b, a / b

# --- 23 ---
def ascii(c):
    return ord(c)

# --- 24 ---
def maiuscula(c):
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while i < 26:
        if c == letras_minusculas[i]:
            return letras_maiusculas[i]
        i += 1
    i = 0
    while i < 26:
        if c == letras_maiusculas[i]:
            return c
        i += 1
    return '*'

# --- 25 ---
def minuscula(c):
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while i < 26:
        if c == letras_maiusculas[i]:
            return letras_minusculas[i]
        i += 1
    i = 0
    while i < 26:
        if c == letras_minusculas[i]:
            return c
        i += 1
    return '*'

# --- 26 ---
def tipo_caracter(c):
    digitos = "0123456789"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    i = 0
    while i < 10:
        if c == digitos[i]:
            return 1
        i += 1

    i = 0
    while i < 26:
        if c == minusculas[i]:
            return 2
        i += 1

    i = 0
    while i < 26:
        if c == maiusculas[i]:
            return 3
        i += 1

    return 4


# --- 27 ---
# A função nacionalidade imprime uma frase com base no país.
# Tem valor por omissão: "Portugal".
# Resultado das chamadas:
# Eu sou de França
# Eu sou de Portugal
# Eu sou de Brasil
# Eu sou de Canadá
def nacionalidade(pais="Portugal"):
    print("Eu sou de " + pais)

nacionalidade("França")
nacionalidade()
nacionalidade("Brasil")
nacionalidade("Canadá")

# --- 28 ---
def asteriscos(n):
    print("*" * n)

# --- 29 ---
def asteriscos_ch(n, ch='*'):
    print(ch * n)

# --- 30 ---
def asteriscos_vertical(n):
    for _ in range(n):
        print("*")

# --- 31 ---
def caracteres(n, ch):
    print(ch * n)

# --- 32 ---
def margem(n):
    if n < 2:
        print("*")
    else:
        print("*" + " " * (n - 2) + "*")

# --- 33 ---
def quadrado(n):
    for _ in range(n):
        print("*" * n)

# --- 34 ---
def triangulo(n):
    for i in range(n):
        estrelas = "*" * (2*i + 1)
        print(estrelas.center(2*n))

# --- 35 ---

def classificacao(nota):
    if 0 <= nota <= 9.4:
        return "Insuficiente"
    elif nota <= 13.4:
        return "Suficiente"
    elif nota <= 17.4:
        return "Bom"
    elif nota <= 20:
        return "Muito Bom"
    else:
        return None

# --- 36 ---

def imc(massa, altura):
    valor = massa / (altura ** 2)
    if valor < 16:
        return "Magreza grave"
    elif valor < 17:
        return "Magreza moderada"
    elif valor < 18.5:
        return "Magreza leve"
    elif valor < 25:
        return "Saudável"
    elif valor < 30:
        return "Sobrepeso"
    elif valor < 35:
        return "Obesidade Grau I"
    elif valor < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# --- 37 ---
def juntar(s1, s2):
    return s1 + s2

# --- 38 ---
def primeira_palavra(frase):
    return frase.split()[0]

# --- 39 ---
def ultima_palavra(frase):
    return frase.split()[-1]

# --- 40 ---
def contar_palavras(frase):
    return len(frase.split())
