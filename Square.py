import turtle

T = turtle.Turtle()


T.penup()
T.goto(-75, 100)
T.pendown()

T.color("black")
T.fillcolor("green")
T.speed(1)

T.begin_fill()
for i in range(4):
    T.forward(200)
    T.right(90)

T.end_fill()
turtle.done()
