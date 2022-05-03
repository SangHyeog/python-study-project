#연습문제 1
print("연습문제 1")
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")

a = turtle.Turtle()
a.color("gray")
a.pensize(5)

startPos = [-490, 100]

for i in range(20, 110, 20):
    a.penup()
    a.goto(startPos[0] + i, startPos[1] + i)
    a.pendown()
    for j in range(4):
        a.forward(120)
        a.left(90)

#연습문제 2
print("연습문제 2")
import turtle

def square(t, size, color):
    t.color(color)
    for i in range(4):
        t.forward(size)
        t.right(90)

t1 = turtle.Turtle()
t1.pensize(5)

startPos = [-190, 340]

t1.penup()
t1.setposition(startPos[0], startPos[1])
t1.pendown()
    
colors = ["red", "orange", "yellow", "green", "blue", "violet", "darkgreen", "hotpink", "grey", "black"]

i = 25
for color in colors:
    square(t1, i, color)
    i = i + 25

#연습문제 3
print("연습문제 3")
import turtle
t = turtle.Turtle()

def drawPolygon(sideLength, numSides, color):
    t.color(color)
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)

startX = 150
startY = 240

t.penup()
t.setposition(startX, startY)
drawPolygon(50, 5, "blue")

t.penup()
t.setposition(startX + 120, startY)
drawPolygon(50, 8, "hotpink")

