import turtle

turtle.bgcolor('white')

T = turtle.Turtle()

T.color("black")
T.pensize(1)

T.hideturtle()

T.penup()
T.goto(-300, 150)
T.showturtle()
T.pendown()

# rectangle in saffron color
T.begin_fill()
T.forward(600)
T.right(90)
T.forward(88)
T.right(90)
T.forward(600)
T.right(90)
T.forward(88)
T.fillcolor('#FF9933')   # saffron color
T.end_fill()
T.begin_fill()

# white rectangle by default because of background screen
T.begin_fill()
T.backward(176)
T.rt(90)
T.forward(600)
T.lt(90)
T.forward(88)
# 3rd rectangle green in color
T.backward(176)
T.lt(90)
T.forward(600)
T.rt(90)
T.forward(88)
T.fillcolor('green')
T.end_fill()


# middle circle

T.penup()
T.home()
T.pendown()
T.pencolor('white')
T.lt(90)
T.backward(22)
T.rt(90)
T.pencolor('blue')
T.pensize(8)
T.circle(40)
T.penup()
T.lt(90)
T.forward(40)
T.rt(90)
T.lt(90)
T.pendown()

# ashok chakra
T.pensize(2)
T.dot(20)
for x in range(24):
    T.forward(40)  # length of spokes
    T.goto(-0, 19)
    T.rt(15)  # angle between spokes
T.penup()
T.rt(90)
T.rt(90)
T.lt(20)
T.forward(220)
T.pencolor('black')
T.begin_fill()
T.end_fill()
T.hideturtle()
T.write('Tawheed', font=("Ani", 30, "bold"))

turtle.done()
