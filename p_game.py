import turtle

#screen set up
wn = turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#SLIDER A

slider_a = turtle.Turtle()
slider_a.speed(0)
slider_a.shape("square")
slider_a.color("yellow")
slider_a.shapesize(stretch_wid=5,stretch_len=1)
slider_a.penup()
slider_a.goto(-350,0)


# Slider B

slider_b = turtle.Turtle()
slider_b.speed(0)
slider_b.shape("square")
slider_b.color("yellow")
slider_b.shapesize(stretch_wid=5, stretch_len=1)
slider_b.penup()
slider_b.goto(350, 0)



#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
# ball.shapesize(stretch_len=2)
# ball.shapesize(stretch_wid=3)
ball.goto(0, 0)
ball.penup()
ball.dx = 0.3
ball.dy = 0.3

# Function for slider moving up

def slider_a_up():
    y = slider_a.ycor()
    y += 30
    slider_a.sety(y)

def slider_a_down():
    y = slider_a.ycor()
    y -= 30
    slider_a.sety(y)

def slider_b_up():
    y = slider_b.ycor()
    y += 30
    slider_b.sety(y)

def slider_b_down():
    y = slider_b.ycor()
    y -= 30
    slider_b.sety(y)


# score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A:0  Player B:0", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 285)
pen.write("Dhaval's game", align="center", font=("Courier", 10, "normal"))

score_a = 0
score_b = 0



wn.listen()
wn.onkeypress(slider_a_up, "w")
wn.onkeypress(slider_a_down, "s")
wn.onkeypress(slider_b_up, "Up")
wn.onkeypress(slider_b_down, "Down")




#  Main loop
while True:
    wn.update()
    #  moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < slider_b.ycor() +40 and ball.ycor() > slider_b.ycor() -40 ):
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < slider_a.ycor() +40 and ball.ycor() > slider_a.ycor() -40 ):
        ball.dx *= -1


