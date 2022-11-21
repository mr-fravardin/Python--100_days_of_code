import time
import turtle as t
import paddle as p
import ball as b
import score as s

WIDTH, HEIGHT = 800, 600

my_screen = t.Screen()
my_screen.tracer(0)
my_screen.title("Pong Game")
my_screen.bgcolor("black")
my_screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT)
my_screen.setup(width=WIDTH+2, height=HEIGHT+2)

# create a paddle
r_paddle = p.Paddle((380, 0))
l_paddle = p.Paddle((-380, 0))
# create a game over turtle for notification
over_object = t.Turtle()
over_object.penup()
over_object.hideturtle()
# create a score object
r_score = s.Scoreboard((30, 260))
l_score = s.Scoreboard((-30, 260))

# create ball
ball = b.Ball((0, 0))

# control the paddle
my_screen.listen()
my_screen.onkey(fun=r_paddle.up, key="Up")
my_screen.onkey(fun=r_paddle.down, key="Down")
my_screen.onkey(fun=l_paddle.up, key="w")
my_screen.onkey(fun=l_paddle.down, key="s")

# moving the paddle
while True:
    time.sleep(ball.ball_speed)
    ball.ball_moving()
    my_screen.update()
    # detecting collision with top and bottom wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.ball_wall_bounce()
    # detect collision with paddles
    if (ball.distance(r_paddle) < 80 and ball.xcor() == 350) or (ball.distance(l_paddle) < 80 and ball.xcor() == -350):
        ball.ball_paddle_bounce()
    # detect if ball was out of bounce and count score
    if ball.xcor() > 390:
        ball.ball_switch()
        l_score.score_plus()
    elif ball.xcor() < -390:
        ball.ball_switch()
        r_score.score_plus()

my_screen.exitonclick()
