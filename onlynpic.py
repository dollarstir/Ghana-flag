#Python Program to draw Olympics logo in Turtle Programming
import turtle
 
bello = turtle.Turtle()
bello.pensize(6) #Set the thickness of the pen 
topCircles = ["blue", "black", "red"] #firstRowColors is a list of colors that are present in the first row of logo
for i in range(3):
  bello.penup()
  bello.pencolor(topCircles[i])
  bello.goto(i*110, 0)
  bello.pendown()
  bello.circle(50)
 
bottomCircles = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  bello.penup()
  bello.pencolor(bottomCircles[i])
  bello.goto(i*55, -50)
  bello.pendown()
  bello.circle(50)