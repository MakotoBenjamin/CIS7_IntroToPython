import turtle

turtle.showturtle()

turtle.speed(1)
turtle.pensize(3)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.setheading(90)
turtle.circle(100, steps = 6)
turtle.end_fill()

turtle.color("white")
turtle.penup()
turtle.goto(50-50,-50/2)
turtle.pendown()
turtle.write("STOP",
        font = ("Times", 50, "bold"),
        align = "center")
turtle.hideturtle()

turtle.done()
