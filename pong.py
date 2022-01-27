
import turtle
wn = turtle.Screen()
wn.title("Pong by Ken")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score keeping
score_a = 0
score_b = 0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = .05

#
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))
#Moving paddles functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_a_diagonal_left():
    x = paddle_a.xcor()
    y = paddle_a.ycor()
    x -= 20
    y += 20
    paddle_a.setx(x)
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_b_right():
        x = paddle_b.xcor()
        x += 20
        paddle_b.setx(x)

def paddle_b_left():
        x = paddle_b.xcor()
        x -= 20
        paddle_b.setx(x)
#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_a_diagonal_left, "q")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_b_right, "Right")
wn.onkeypress(paddle_b_left, "Left")
# Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle border checking
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    if paddle_b.xcor() > 390:
        paddle_b.setx(390)
    if paddle_b.xcor() < -390:
        paddle_b.setx(-390)
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_a.xcor() < -390:
        paddle_a.setx(-390)
    if paddle_a.xcor() > 390:
        paddle_a.setx(390)


    # Ball Border checking
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
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if paddle_a.xcor() > 350:
        paddle_a.goto(-350, 0)
        score_a += 2
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if paddle_b.xcor() < -350:
        paddle_b.goto(350, 0)
        score_a += 2
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #Paddle and ball collisions
    #if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
     #   ball.setx(340)
      #  ball.dx *= -1
    if(ball.xcor() > paddle_b.xcor() -20) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(paddle_b.xcor() -20)
        ball.dx *= -1
    if (ball.xcor() < paddle_a.xcor() + 20) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(paddle_a.xcor() + 20)
        ball.dx *= -1
    if (paddle_a.xcor() < 0 ) and (paddle_b.ycor() < paddle_a.ycor() + 100 and paddle_b.ycor() > paddle_a.ycor() - 100 and paddle_b.xcor() < paddle_a.xcor() -10):
        paddle_b.goto(350, 0)
        score_b -= 3
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if (paddle_b.xcor() > 0 ) and (paddle_a.ycor() < paddle_b.ycor() + 100 and paddle_a.ycor() > paddle_b.ycor() - 100 and paddle_a.xcor() > paddle_b.xcor() +10):
        paddle_a.goto(-350, 0)
        score_a -= 3
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
