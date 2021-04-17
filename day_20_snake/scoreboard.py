from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
