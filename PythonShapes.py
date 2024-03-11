#Harry Newman, Python Shapes Program, IMA Application, 12/07/22;

import turtle
import os
import random
turtle.setup(500,500)


def convert(b):
    j = list(b.split(" "))
    return j

def placechecker():
    while True:
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        place = (x, y)
        splace = str(place)
        return place
        break

turtle.tracer(0)

def square(size, place, color):
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.penup()
    turtle.end_fill()

def triangle(size, place, color):
    size9 = size * 0.85
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(65)
    turtle.forward(size)
    turtle.right(130)
    turtle.forward(size)
    turtle.right(115)
    turtle.forward(size9)
    turtle.penup
    turtle.end_fill()


def oval(size, place, color):
    size6 = size * 0.6
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size, 360/2.5)
    turtle.forward(size)
    turtle.circle(size, 720/3.85)
    turtle.forward(size6)
    turtle.end_fill()


def circle(size, place, color):
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size, 360)
    turtle.penup()
    turtle.end_fill()
    
def star(size, place, color):
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(90)
    count = 0
    while True:
        turtle.forward(size)
        turtle.left(170)
        count += 1
        if count == 37:
            break
    turtle.end_fill()

def diamond(size, place, color):
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(size)
        turtle.left(45)
        turtle.forward(size / 1.414)
        turtle.left(135)
    turtle.end_fill()


    
def idek(size, place, color):
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(90)
    count = 0
    while True:
        turtle.forward(size)
        turtle.left()
        count += 1
        if count == 18:
            break
    turtle.end_fill()

def hexagon(size, place, color):
    turtle.penup()
    turtle.goto(place)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(6):
       turtle.forward(size)
       turtle.left(300)
    turtle.end_fill()


count = 0
times = random.randint(200, 400)

blist = ['yellow','gold','orange','red','maroon','violet','magenta','purple','navy','blue','skyblue','cyan','turquoise','lightgreen','green','darkgreen','chocolate','brown','black','gray','teal','firebrick','darkslategray','deeppink']
backgroundnum = random.randint(0,22)
background = blist[backgroundnum]
turtle.bgcolor(background)
blist.remove(blist[backgroundnum])
for joe in range(times):
    colornum = random.randint(0,(len(blist)-1))
    color = blist[colornum]

    size = random.randint(30,125)
    place = placechecker()
    splace = str(place)
    shapes = random.randint(1,9)
    if shapes == 1:
        shapes == circle
        circle(size, place, color)
    if shapes == 2:
        shapes == square
        square(size, place, color)
    if shapes == 3:
        shapes == star
        star(size, place, color)
    if shapes == 4:
        shapes == oval
        oval(size, place, color)
    if shapes == 5:
        shapes == triangle
        triangle(size, place, color)
    if shapes == 6:
        shapes == idek
        star(size, place, color)
    if shapes == 7:
        shapes == hexagon
        hexagon(size, place, color)
    if shapes == 8:
        shapes == diamond
        diamond(size, place, color)

turtle.update()
