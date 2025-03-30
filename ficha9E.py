# Ficha de Trabalho 9

# 1. Tipos de dados conhecidos: inteiros, reais, texto, booleanos, listas, tuplos, dicionários, conjuntos.

# 2. Não. Existem mais tipos, incluindo personalizados e outros mais complexos.

# 3. Python: int, float, str, bool, list, tuple, dict, set, NoneType.

# 4. Array é estrutura com vários elementos acedidos por índice.

# 5. Vetor é array com 1 dimensão; tabela pode ter 2 ou mais

# 6. Python usa listas como arrays.

# 7. Lista é coleção ordenada e mutável de elementos.

# 8 a)
vetor = [1, 5, 25, 123, 72]
# 8 b)
vetor[0] = 199
# 8 c)
vetor[4] = 250
# 8 d)
valor = int(input("Novo valor para a segunda posição: "))
vetor[1] = valor
# 8 e)
print("Último valor:", vetor[4])
# 8 f)
vetor_10 = [0,0,0,0,0,0,0,0,0,0]
# 8 g)
vetor_reais = [0.0,0.0,0.0,0.0]

# 9. Lista é alterável; tuplo é fixo após criação.

# 10
vetor = (1, 4, 7, 12, 9, 2, 5, 16, 99, 2)
i = 0
while i < len(vetor):
    print(vetor[i], end=" ")
    i += 1
print()

# 11
numeros = []
i = 0
while i < 5:
    n = int(input("Número: "))
    numeros.append(n)
    i += 1

i = 0
while i < 5:
    if i < 4:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])
    i += 1

# 12
i = 4
while i >= 0:
    if i > 0:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])
    i -= 1

# 13: usamos if para não mostrar vírgula no fim

# 14
# a) range(5): sequência de 0 a 4
# b) tuplo (valores fixos)
# c) lista (valores podem mudar)
# d) conjunto (valores únicos, sem ordem)

# 15
procurado = int(input("Número a procurar: "))
encontrado = False
i = 0
while i < len(numeros):
    if numeros[i] == procurado:
        encontrado = True
    i += 1
if encontrado:
    print("Existe na lista")
else:
    print("Não existe na lista")

# 16
valores = []
i = 0
while i < 10:
    valor = int(input("Insere número entre 1 e 20: "))
    if valor >= 1 and valor <= 20:
        valores.append(valor)
        i += 1
    else:
        print("Fora dos limites!")

n = int(input("Número a procurar: "))
encontrado = False
j = 0
while j < len(valores):
    if valores[j] == n:
        encontrado = True
    j += 1
if encontrado:
    print("Número encontrado")
else:
    print("Número não encontrado")

# 17
i = 0
encontrado = False
while i < len(valores):
    if valores[i] == n:
        print("Encontrado na posição:", i)
        encontrado = True
        break
    i += 1
if not encontrado:
    print("Não existe")

# 18
i = 0
ocorrencias = 0
while i < len(valores):
    if valores[i] == n:
        print("Encontrado na posição:", i)
        ocorrencias += 1
    i += 1
print("Total de ocorrências:", ocorrencias)

# 19
valores = []
i = 0
while i < 10:
    v = int(input("Número: "))
    valores.append(v)
    i += 1

soma = 0
i = 0
while i < 10:
    soma += valores[i]
    i += 1
media = soma / 10
print("Média:", media)

# 20
i = 0
while i < 10:
    if valores[i] < media:
        valores[i] = 0
    i += 1
print("Valores após substituição:", valores)

# 21
contagem = [0, 0, 0, 0, 0, 0]
i = 0
while i < 1000:
    dado = (i % 6) + 1  # simula de forma previsível
    contagem[dado - 1] += 1
    i += 1

print("Contagens de 1 a 6:")
i = 0
while i < 6:
    print(i+1, "saiu", contagem[i], "vezes")
    i += 1

# 22
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print("Os meses que têm 30 dias são:")
i = 0
while i < len(meses):
    if meses[i] == "Abril" or meses[i] == "Junho" or meses[i] == "Setembro" or meses[i] == "Novembro":
        print(meses[i])
    i += 1

# 23 a)
chave = []
i = 0
while i < 5:
    num = int(input("Número entre 1 e 50: "))
    if num >= 1 and num <= 50:
        chave.append(num)
        i += 1
estrelas = []
i = 0
while i < 2:
    num = int(input("Estrela entre 1 e 11: "))
    if num >= 1 and num <= 11:
        estrelas.append(num)
        i += 1
print("Chave:", chave)
print("Estrelas:", estrelas)

# 23 b)
chave = []
i = 0
while i < 5:
    num = int(input("Número entre 1 e 50 (sem repetição): "))
    if num >= 1 and num <= 50 and not (num in chave):
        chave.append(num)
        i += 1
estrelas = []
i = 0
while i < 2:
    num = int(input("Estrela entre 1 e 11 (sem repetição): "))
    if num >= 1 and num <= 11 and not (num in estrelas):
        estrelas.append(num)
        i += 1
print("Chave:", chave)
print("Estrelas:", estrelas)

# 24
kg = [45, 51, 49, 64, 78, 59]
soma = 0
i = 0
while i < len(kg):
    soma += kg[i]
    i += 1
media = soma / len(kg)
print("A soma de todos os elementos do vetor kg é", soma)
print("A média de kg dos valores registados no vetor é", media)

# 25
valores = []
i = 0
while i < 10:
    v = int(input("Número: "))
    valores.append(v)
    i += 1
soma = 0
maximo = valores[0]
minimo = valores[0]
i = 0
while i < 10:
    soma += valores[i]
    if valores[i] > maximo:
        maximo = valores[i]
    if valores[i] < minimo:
        minimo = valores[i]
    i += 1
media = soma / 10
print("Soma:", soma)
print("Média:", media)
print("Máximo:", maximo)
print("Mínimo:", minimo)

# 26
n = int(input("Quantos valores quer inserir? "))
valores = []
i = 0
while i < n:
    v = int(input("Número: "))
    valores.append(v)
    i += 1
soma = 0
i = 0
while i < n:
    soma += valores[i]
    i += 1
media = soma / n
print("Soma:", soma)
print("Média:", media)
