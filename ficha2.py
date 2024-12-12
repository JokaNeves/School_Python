""""
#EX 1 
#print("Bom dia!")

#EX 2
#a=input("Como te chamas?")
#print("olá", a)

#EX 3
#a=input("Primeiro nome: ")
#b=input("Apelido: ")
#print("o teu nome completo é ", a, b)

#EX 4
a=int(input("Intruduz um número: "))
print("O teu número intruduzido foi:", a)

#EX 5
a=int(input("Intruz um número: "))
print("O dobro do teu número é: ", a*2)

#EX 6
a=int(input("Intruz um número: "))
print("O dobro do teu número é: ", a*2)

#EX 7
a=int(input("Intruz um número: "))
print("O dobro de", a, "é", a*2)

#EX 8
a=int(input("Intruz o primeiro número: "))
b=int(input("Intruz o segundo número: "))
print("A multiplicação entre os dois números é:", a*b)

#EX 9
a=int(input("Intruz o primeiro número: "))
b=int(input("Intruz o segundo número: "))
print("A divisão do primeiro pelo segundo é:", a/b)
print("A divisão do segundo pelo primeiro é:", b/a)

#EX 10
a=int(input("Intruz o primeiro número: "))
b=int(input("Intruz o segundo número: "))
print("A divisão do primeiro pelo segundo é:", a//b)
print("A divisão do segundo pelo primeiro é:", b//a)

#EX 11
a=int(input("Intrduz o primeiro número: "))
b=int(input("Intrduz o segundo número: "))
print("Resultado:\n","Soma = ",a+b,"\nSubtração = ",a-b,"\nDivisão = ",a/b,"\nMultiplicação = ",a*b)

#Exercício12
numero1= int(input("Escreve um numero: "))
numero2= int(input("Escreve um numero: "))
r1=numero1/numero2
r2=numero1//numero2
r3=numero1 % numero2
print("Divisão(real): ", r1,"\nDivisão(inteira): ", r2,"\nResto: ", r3)

#Exercício13
a= int(input("Escreve um numero: "))
b= int(input("Escreve um numero: "))
print("a: ", a,"\nb:", b)
a, b = b, a
print("a: ", a,"\nb:", b)

#Exercício14
n=input("Escre algo:")
if type(n) == int:
    print("A váriavel é um número inteiro")
elif type(n) == str:
    print("A váriavel é uma String")
else:
    print("Não é Número inteiro nem String")
"""