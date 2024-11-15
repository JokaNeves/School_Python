
#Exercico 1
#import turtle
#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.right(90)
#quadrado(100)

#Exercicio 2
#import turtle
#def quadrado(n):
#    for i in range(4):
#      turtle.forward(n)
#      turtle.right(90)
      
#for i in range(10,101,10):
#    quadrado(i)

#def quadrado(n):
#    for i in range(4):
#      turtle.backward(n)
#      turtle.right(90)

#for i in range(10,101,10):
#    quadrado(i)

#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.right(90)
        
#for i in range(10, 101, 10):
#    quadrado(i)
#    turtle.penup()
#    turtle.forward(i+10)
#    turtle.pendown()

#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.right(90)
#lado=250
#for i in range(5):
#    quadrado(lado)
#    turtle.penup()
#    turtle.forward(25)
#     turtle.right(90)
#    turtle.forward(25)
#    turtle.left(90)
#    turtle.pendown()
#    lado-=50

#Exercicio 3
#import turtle
#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.right(90)
#color = ['gray', 'violet', 'blue', 'yellow', 'red']
#lado=250
#
#for i in range(5):
#    turtle.fillcolor(color[i])
#    turtle.begin_fill()
#    quadrado(lado)
#    turtle.end_fill()
#    turtle.penup()
#     turtle.forward(25)
#     turtle.right(90)
#     turtle.forward(25)
#     turtle.left(90)
#     turtle.pendown()
#     lado -=50
       
#exercicio 4
#import turtle
#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.right(90)
#        
#for i in range(10, 201,10):
#    quadrado(i+1)
#    turtle.right(18)

#exercicio 5
#import turtle
#def triangulo(n):
#    for i in range(3):
#        turtle.left(120)
#        turtle.forward(n)
#        
#for i in range(6):
#    turtle.left(60)
#    triangulo(100)

#Exercicio 6
#import turtle
#turtle.setpos(150,0)
#turtle.left(90)
#turtle.fillcolor("black")
#turtle.begin_fill()
#turtle.circle(150)
#turtle.end_fill()

#turtle.setpos(0,0)
#turtle.right(90)
#turtle.right(20)
#turtle.penup()
#turtle.fillcolor("white")
#turtle.begin_fill()
#for i in range (3):
#    turtle.forward(250)
#    turtle.left(120)
#turtle.end_fill()
#turtle.setpos(20,80)
#turtle.begin_fill()
#turtle.circle(20)
#turtle.end_fill()
    
#Exercicio 7
#import turtle
#import math as m
#cateto1 = int(input("Medida do primeiro cateto:"))
#cateto2 = int(input("Medida do segundo cateto:"))
#hipotenusa = pow(cateto1**2+ cateto2**2, 0.5)
#angulo1= m.degrees(m.asin(cateto1 / hipotenusa))
#angulo2= m.degrees(m.asin(cateto2 / hipotenusa))

#turtle.forward(cateto2)
#turtle.left(180-angulo1)
#turtle.forward(hipotenusa)
#turtle.left(180-angulo2)
#turtle.forward(cateto1)

#Exercicio 8
#import turtle
#import math as m
#base=int(input("Indique a medida da base:"))
#lado=int(input("indique a medida dos lados:"))
#while 2*lado<=base:
#    print("Medidas impossiveis, medida dos lados deve ser superior ao dobro da medida da base")
#    base=int(input("Indique a medida da base:"))
#    lado=int(input("indique a medida dos lados:"))
#angulo1=m.degrees(m.acos(base/2/lado))
#angulo2=180-(2*angulo1)
#turtle.forward(base)
#turtle.left(180-angulo1)
#turtle.forward(lado)
#turtle.left(180-angulo2)
#turtle.forward(lado)

#exercicio 9
#import turtle
#import math as m
#def triangulo(turtle, base, altura):
#    hipotenusa=(base**2+altura**2)**0.5
#    turtle.forward(base)
#    turtle.left(160)
#    turtle.forward(hipotenusa)
#    turtle.left(110)
#    turtle.forward(altura)
#    turtle.left(90)
#for i in range(3):
#    triangulo(turtle, 300, 110)
#    turtle.right(120)

#Exercicio 10
#import turtle
#import math as m
#def triangulo(turtle, base, altura):
#    angulo1=m.degrees(m.acos((2*altura**2-base**2)/(2*altura**2)))
#    angulo2=(180-angulo1)/2
#    turtle.forward(base)
#    turtle.left(180-angulo2)
#    turtle.forward(altura)
#    turtle.left(180-angulo1)
#    turtle.forward(altura)
#    turtle.left(180-angulo2)

#base=100
#altura=300
#for i in range (10):
#    triangulo(turtle, base, altura)
#    turtle.right(36)
