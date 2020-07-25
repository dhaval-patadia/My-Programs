import turtle

# screen set up
wn = turtle.Screen()
wn.title("Ball Slider")
wn.setup(width=600, height=500)
wn.tracer(0)
wn.bgcolor("black")

#  Slider

slider = turtle.Turtle()
slider.shape("square")
slider.color("Yellow")
slider.shapesize(stretch_wid=1, stretch_len=5)
slider.penup()
slider.goto(0, -220)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.dx = 0.15
ball.dy = 0.15


# slider movement:

#slider right
def slider_right():
    x = slider.xcor()
    x += 30
    slider.setx(x)

#slider left
def slider_left():
    x = slider.xcor()
    x -= 30
    slider.setx(x)

# Keyboared connectivity
wn.listen()
wn.onkeypress(slider_right, "d")
wn.onkeypress(slider_left, "a")

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Score:0", align="center", font=("Courier", 15, "normal"))
pen.goto(-220, 220)
pen.write("Dhaval's game", align="center", font=("Courier", 10, "normal"))

Score = 0



#  Main loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Boundry checking
    if ball.ycor() > 230:
        ball.sety(230)
        ball.dy *= -1
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    if ball.ycor() < -230:
        ball.goto(0, 0)
        ball.dx *=-1
        ball.dy *=-1
        pen.clear()
        Score=0



    #  Ball collision with slider

    if ((ball.ycor() < -200 and ball.ycor()>-205) and (ball.xcor() > slider.xcor()-46 and ball.xcor() < slider.xcor() +46)):
        ball.dy *= -1
        Score += 1
        pen.clear()
        pen.goto(0, 220)
        pen.write("Score:{}".format(Score), align="center", font=("Courier", 15, "normal"))





