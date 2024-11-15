#Exercício1
#import turtle

#turtle.forward(50)

#Exercício
#import turtle

#turtle.right(90)
#turtle.forward(50)

#Exercício3
#import turtle

#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
#turtle.forward(50)
#turtle.right(90)
    
#Exercício4
#import turtle

#turtle.right(60)
#turtle.forward(100)
#turtle.right(120)
#turtle.forward(100)
#turtle.right(120)
#turtle.forward(100)

#Exercício5
#import turtle

#turtle.right(60)
#for i in range(2):
 #   turtle.forward(100)
#    turtle.right(120)
    
#turtle.forward(100)

#Exercício6
#import turtle

#for i in range(4):
#    turtle.forward(50)
#    turtle.right(90)
    
    
#Exercício7
#import turtle

#turtle.circle(200)

#Exercício8
#import turtle

#for i in range(4):
#  turtle.circle(100)
#  turtle.penup()
#  turtle.forward(200)
#  turtle.pendown()
  

#Exercício9
#import turtle
#turtle.fillcolor ("blue")
#turtle.begin_fill()
#turtle.circle(50)
#turtle.end_fill()
#turtle.penup ()
#turtle.forward(100)
#turtle.pendown
#turtle.fillcolor ("yellow")
#turtle.begin_fill()
#turtle.circle (50)
#turtle.end_fill()
#turtle.penup()
#turtle.forward(100)
#turtle.pendown()
#turtle.fillcolor ("pink")
#turtle.begin_fill()
#turtle.circle(50)
#turtle.end_fill()
#turtle.penup()
#turtle.forward(100)
#turtle.pendown()
#turtle.fillcolor ("red")
#turtle.begin_fill()
#turtle.circle(50)
#turtle.end_fill()


#Exercício10
#import turtle

#for i in range (5):
# turtle.forward(100)
# turtle.left(72)
 
#Exercício11
#import turtle
#l=int(input("Quantos lados tem?"))

#for i in range (l):
# turtle.forward(100)
# turtle.right(360/l)
 
 
#Exercício12
#import turtle

#for i in range(24):
#    for i in range(4):
#        turtle.forward(100)
#        turtle.right(90)
#    turtle.left(18)

#Exercício13
import turtle

turtle.penup()
for a in range(40, -1, -1):
    turtle.stamp()
    turtle.left(a)
    turtle.forward(20)