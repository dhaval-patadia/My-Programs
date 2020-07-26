import turtle
import time
import random


delay = 0.08
score = 0
high_score = 0
# screen set up
wn=turtle.Screen()
wn.title("Snake Game By Dhaval")
wn.setup(width=500, height=500)
wn.bgcolor("Black")

# snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("Yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food Placement
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(150, 150)

segments = []

# scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 210)
pen.write("score:{} high_score:{}".format(score, high_score), align="center", font=("arial",21,"italic"))





def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_left():
    if head.direction != "right":
        head.direction  ="left"

def go_right():
    if head.direction != "left":
        head.direction  ="right"


# Funtion to move
def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)


    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#key board settings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")



#main Loop
while True:
    wn.update()

    if head.xcor()>230 or head.xcor()<-230 or head.ycor()>230 or head.ycor()<-230:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("score:{} high_score:{}".format(score, high_score), align="center", font=("arial",21,"italic"))


    if head.distance(food) < 20:
        x = random.randint(-240, 240)
        y = random.randint(-240, 200)
        food.goto(x,y)

        # adding segments
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("grey")
        new_segments.penup()
        segments.append(new_segments)

        # minimize the delay
        delay -= 0.001
        # scoring
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score:{} high_score:{}".format(score, high_score), align="center", font=("arial",21,"italic"))


    # to move the segments to previous segment position

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    # checking the collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("score:{} high_score:{}".format(score, high_score), align="center", font=("arial",21,"italic"))




    time.sleep(delay)
wn.mainloop()