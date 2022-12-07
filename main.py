import turtle

myFirstTurtle = turtle.Turtle()
mySecondTurtle = turtle.Screen()
mySecondTurtle.title("")
mySecondTurtle.setup(width=720, height=420)
mySecondTurtle.bgcolor("red")

myFirstTurtle.up()
myFirstTurtle.goto(-100, -100)
myFirstTurtle.color('white')
myFirstTurtle.begin_fill()
myFirstTurtle.circle(120)
myFirstTurtle.end_fill()

myFirstTurtle.goto(-70, -80)
myFirstTurtle.color('red')
myFirstTurtle.begin_fill()
myFirstTurtle.circle(100)
myFirstTurtle.end_fill()

myFirstTurtle.goto(0, 35)
myFirstTurtle.fillcolor("white")
myFirstTurtle.begin_fill()

for i in range(5):
    myFirstTurtle.forward(150)
    myFirstTurtle.right(144)
myFirstTurtle.end_fill()

myFirstTurtle.goto(-130, -190)
myFirstTurtle.color("white")
myFirstTurtle.write("TURKEY", font=("Verdana", 17, "bold"))

myFirstTurtle.goto(-999, -0)

mySecondTurtle.exitonclick()
from turtle import *

red = "#FF0000"
white = "#FFFFFF"
yellow = "#FFFF00"

pencolor(red)
fillcolor(red)

begin_fill()
forward(150)
left(90)
forward(300)
left(90)
forward(150)
left(90)
forward(300)
end_fill()

pencolor(white)
fillcolor(white)
begin_fill()
up()
forward(75)
right(90)
forward(150)
left(90)
down()
circle(75)
end_fill()

pencolor(yellow)
fillcolor(yellow)
begin_fill()
up()
forward(65)
right(162)
down()

for i in range(5):
    forward(60)
right(144)
end_fill()

done()
