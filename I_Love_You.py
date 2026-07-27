import turtle

def draw_heart():
    screen = turtle.Screen()
    screen.title("I Love You")
    screen.bgcolor("black")
    screen.tracer(1)
    screen.delay(2)
    

    pen = turtle.Turtle()
    pen.color("red", "pink")
    pen.pensize(3)

    pen.begin_fill()
    pen.left(140)
    pen.forward(111.65)

    for i in range(200):
        pen.right(1)
        pen.forward(1)

    pen.left(120)

    for i in range(200):
        pen.right(1)
        pen.forward(1)

    pen.forward(111.65)
    pen.end_fill()

    pen.hideturtle
    pen.up()        
    pen.goto(0,-50)

    pen.color("white")
    style= ("Baguet script", 20, "bold")
    pen.write("I Love You", font=style, align="center")
    pen.speed(2)

    screen.mainloop

if __name__ == "__main__":
    draw_heart()    