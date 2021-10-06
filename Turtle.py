import turtle
import math

turtle.shape('turtle')
'''
turtle.forward(100)
turtle.left(30)
turtle.forward(150)
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

n=50
a=((n-2)/n)*180
for i in range(n):
    turtle.forward(20)
    turtle.left(180-a)

turtle.penup()    
turtle.goto(200,-100)
turtle.pendown()

d=10
for i in range(10):
    for kv in range(3):
        turtle.forward(d)
        turtle.right(90)
    turtle.forward(d)
    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.right(180)
    d+=10

turtle.penup()    
turtle.goto(-100,-100)
turtle.pendown()

lp=12
a=360/lp
for i in range(lp):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(a)
'''
pi=math.pi
n=580
dfi=(2*pi)/90
fi=dfi
k=10
for i in range(n):
    turtle.forward(k*dfi*((1+fi)**0.5))
    turtle.left((dfi*180)/pi)
    fi+=dfi
