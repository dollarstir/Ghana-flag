# importing turtle class
import turtle


# function for creating rectangles in ghana flag

def rectangle(mycolor):
    bello.begin_fill()
    bello.fillcolor(mycolor)
    for i in range(2):
        bello.forward(400)
        #making angle of 90 from top right of the cartesian plane
        bello.right(90)
        bello.forward(100)
        bello.right(90)
        # bello.forward(350)
        # bello.right(90)
    bello.end_fill()

def mystar():
    rg = 0
    bello.speed(1)
    # bello.bgcolor("black")
    bello.begin_fill()
    bello.fillcolor('black')
    while rg < 5 :
        bello.forward(45)
        bello.right(145)
        rg = rg + 1

    bello.end_fill()


    




#creating instance of Turtle class
bello = turtle.Turtle() 

#Moving the the drawing pen down
bello.up()

#moving to a position 0  on e axis and -300 on y axis
bello.goto(0,-300)

# about to draw
bello.down()

#Draw straightline from posiitino (0,-300) to position (0,300)
bello.goto(0,300)
rectangle("red")
bello.goto(0,200)
# bello.forward(400)
rectangle("yellow")
bello.goto(0,100)
rectangle("green")
bello.hideturtle()
bello.up()
bello.goto(150,200)
bello.up()
bello.goto(150,150)

bello.down()

mystar()


# blackstar()
# rectangle("yellow")
# bello.goto(0,100)
# rectangle("green")



