from turtle import Turtle


FONT = ('arial', 18, 'normal')


try:
    score = int(open('high_score.txt', mode='r').read())
except FileNotFoundError:
    score = open('high_score.txt', mode='w').write(str(0))
except ValueError:
    score = 0


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.high_score = score
        self.goto(x=-580, y=260)
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.high_score} "
                   f"Live: {self.lives}", font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open('high_score.txt', mode='w').write(str(self.high_score))
