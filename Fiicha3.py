#Exercício1
#a=int(input("Introduz um número: "))
#b=int(input("Introduz outro número: "))
#if a == b:
#   print("Os número introduzidos são iguais.")
#else:
#    print(" ")

#Exercício2
#a=int(input("Introduz um número: "))
#b=int(input("Introduz outro número: "))
#if a == b:
 #   print("Os número introduzidos são iguais.")
#else:
 #   print("Os números introduzidos são diferentes.")
 
#Exercício3
#n = int(input("Introduz um número: "))
#if n>0:
 #   print("O número introduzido é positivo.")
#elif n == 0:
#    print("O número introduzido é nulo.")
#else:
#    print("O número introduzido é negativo.")
    
#Exercício4
#c = float(input("Qual é a temperatura da água(Graus C)?: "))
#if c<=0:
 #   print("A água está no estado sólido.")
#elif 0<c<100:
 #   print("A água está no estado líquido.")
#else:
 #   print("A água está no estado gasoso.")
    
#Exercício5
#a=int(input("Introduz um número: "))
#b=int(input("Introduz outro número: "))
#if a>b:
#    print("O número" ,a, "é o maior.")
#elif a==b:
#    print("Ambos os números têm os mesmo valor.")
#else:
#    print("O número" ,b, "é o maior.")

#Exercicio 6
#num=int(input("Introduz um número:"))
#if num%2==0:
#     print("O número é par.")
#else:
#     print("O número é ímpar.")
     
#Exercício7
# num1=int(input("Introduz um número:"))
# if num1%2==0:
#      print("O número é par.")
# else:
#      print("O número é ímpar.")
# print("")
# num2=int(input("Intruduz um número:"))
# if num2%2==0:
#      print("O número é par.")
# else:
#      print("O número é ímpar.")
     
#Exercício8
#for i in range(1,10):
#    print(i)
    
#Exercício9
#i=int(input("Introduz um número:"))
#x=range(0,i)
#for valor in x:
#    print(valor+1)

#Exercício10
#i=int(input("Introduz um número:"))
#x=range(i,0, -1)
#for valor in x:
#  print(valor)

#Exercício11
#n1=int(input("Introduz um número(menor):"))   
#n2=int(input("Introduz um número(maior):"))
#x=range(n1,n2+1,1)
#for valor in x:
#    print(valor)

#Exercício12
#n1=int(input("Introduz um número(maior):"))   
#n2=int(input("Introduz um número(menor):"))
#x=range(n1,n2-1,-1)
#for valor in x:
#   print(valor)

#Exercício13
#n1=int(input("Introduz um número(menor):"))   
#n2=int(input("Introduz um número(maior):"))
#x=range(n1,n2+1,2)
#for valor in x:
#    print(valor)
    
#Exercício14
#n1=int(input("Introduz um número(maior):"))   
#n2=int(input("Introduz um número(menor):"))
#x=range(n1,n2-1,-5)
#for valor in x:
#   print(valor)

#Exercício15
#i=int(input("Introduz um número:"))    
#for t in range(1,11):
#    print(i,"X",t,"=",i*t,"\n")
    
#Exercício16
#i=int(input("Introduz um número:"))
#n1=int(input("Introduz o múltiplo inicial:"))
#n2=int(input("Introduz o múltiplo final:"))
#for t in range(n1,n2+1):
#    print(i,"X",t,"=",i*t,"\n")

#Exercício17
#n1=int(input("Introduz o número inicial:"))
#n2=int(input("Introduz o número final:"))
#for x in range(n1,n2):
#     if x % 2 == 0:
#       print(x)
       
#Exercício18
#n1=int(input("Introduz o número inicial:"))
#n2=int(input("Introduz o número final:"))
  
#contador = 0  
#for x in range(n1,n2+1):
#     if x % 2 == 0:
#         contador += 1
         
#print("Existem", contador, "números pares entre", n1, "e", n2)
         
#Exercício19
#n1=int(input("Introduz o número inicial:"))
#n2=int(input("Introduz o número final:"))
  
#contador = 0  
#for x in range(n1,n2+1):
#     if x % 2 != 0:
#         contador += 1
         
#print("Existem", contador, "números ímpares entre", n1, "e", n2)
         
#Exercício20
#i=int(input("Introduz um número:"))

#while i!=0:

#if i%2==0:
#    print("O nº", i,"é par.")
#else:
#   print("O nº", i,"é ímpar.")
   
#   i=int(input("Introduz um número:"))
   
#Exercício21
#i=int(input("Introduz um número:"))
#contador = 0

#for num in range(1, i+1):
    #print(num)
# if i % num == 0:
#    contador += 1
#    print("Divísivel por", num)
#if contador == 2:
#    print("É primo.")
#else:
#    print("Não é primo.")
    
#Exercício22
n1=int(input("Introduz um número(inferior):"))   
n2=int(input("Introduz um número(superior):"))

print("")

contador = 0
contadorpar = 0
contadorimpar = 0  
contadorprimos = 0
primo=0
x=range(n1, n2+1)
for i in x:
   contador+=1
   y=range(1, i+1)
   for a in y:
       if i%a==0:
           primo+=1
   if primo==2:
       contadorprimos+=1
   primo=0
   if i%2==0:
       contadorpar+=1
   elif i%2!=0:
       contadorimpar+=1
   else:
       print("")

print("Existem entre", n1,"e",n2,",", contador,"números.")
print("Existem entre", n1,"e",n2,",", contadorpar,"números pares.")
print("Existem entre", n1,"e",n2,",", contadorimpar,"números ímpares.")       
print("Existem entre", n1,"e",n2,",", contadorprimos,"números primos.")   
   
   
   
  
    
    
