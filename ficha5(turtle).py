#Exercício1
#import turtle

#def quadrado(n):
#    turtle.right(90)
#    turtle.forward(n)
   
#for i in range(4):
#    quadrado(100)
   
#Exercício2.1
#import turtle

#def quadrado(n):
#    for i in range(4):
#       turtle.right(90)
#      turtle.forward(n)
       
#for x in range(10,101,10):
#    quadrado(x)
   
   
#Exercício2.2
#import turtle

#def quadrado(n):
#    for i in range(4):
#      turtle.right(90)
#      turtle.forward(n)

#for x in range(100,9,-10):
#    quadrado(x)
   
#Exercício2.3
#import turtle

#def quadrado(n):
#    for i in range(4):
#      turtle.right(90)
#      turtle.forward(n)
     
#for x in range(10,101,10):
#    quadrado(x)
#    turtle.penup()
#    turtle.forward(x+20)
#    turtle.pendown()
   

#Exercício2.4
#import turtle

#def quadrado(n):
#    for i in range(4):
#        turtle.forward(n)
#        turtle.left(90)

#lado = 250
     
#for x in range(5):
#     quadrado(lado)
#     turtle.penup()
#     turtle.forward(25)
#     turtle.left(90)
#     turtle.forward(25)
#     turtle.right(90)
#     turtle.pendown()
#     lado -= 50
   
#exercício3
#import turtle

#def quadrado(n):
 #   for i in range(4):
 #       turtle.forward(n)
 #       turtle.left(90)

#\color = ['gray', 'violet', 'blue', 'yellow', 'red']
#lado= 250

#for i in range(5):
#    turtle.fillcolor(color[i])
#    turtle.begin_fill()
#    quadrado(lado)
#    turtle.end_fill()
#    turtle.penup()
#    turtle.forward(25)
#    turtle.left(90)
#   turtle.forward(25)
#    turtle.right(90)
#    turtle.pendown()
#    lado -= 50

#exercício4
#import turtle

#def quadrado(n):
#    for x in range(4):
#        turtle.forward(n)
#        turtle.left(90)
       
#for i in range(10, 201, 10):
#    quadrado(i+10)
#    turtle.right(18)
   
#exercício5
#import turtle

#def triangulo(n):
#    for i in range(3):
#        turtle.left(120)
#        turtle.forward(n)
       
#for i in range(6):
#    turtle.left(60)
#    triangulo(100)

#exercicio 6
import turtle as t

def circulo_grande():
    t.fillcolor("black")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.left(90)
    t.forward(100)
    t.right(60)

def triangulo():
    t.fillcolor("white")
    t.begin_fill()
    t.forward(100)
    t.right(60)
    t.color("white")
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.end_fill()

def mini_circulo():
    t.color("black")
    t.right(60)
    t.forward(35)
    t.right(90)
    t.forward(30)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

circulo_grande()
triangulo()
mini_circulo()
