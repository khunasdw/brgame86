from turtle import Screen, Turtle
from blocks import Bricks
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import turtle


screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Break Out Game")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
score = Scoreboard(lives=5)


game_is_on = True
game_pause = False


def pause_game():
    global game_pause
    if game_pause:
        game_pause = False
    else:
        game_pause = True


screen.listen()
screen.onkey(fun=paddle.go_left, key="Left")
screen.onkey(fun=paddle.go_right, key="Right")
screen.onkey(key="space", fun=pause_game)


def check_collision_with_walls():

    global ball, game_is_on, score

    if ball.xcor() < -580 or ball.xcor() > 580:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            game_is_on = False
            return
        return


def check_collision_with_paddle():

    global ball, paddle

    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 100 and ball.ycor() < -250:

        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collision_with_bricks():
    global ball, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.clear()
            score.increase_score()
            brick.goto(3000, 3000)
            bricks.bricks.remove(brick)

            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while game_is_on:

    screen.update()
    ball.move()

    check_collision_with_walls()
    check_collision_with_paddle()
    check_collision_with_bricks()


turtle.mainloop()
