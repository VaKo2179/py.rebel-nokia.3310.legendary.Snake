from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(arg=f"Score: {self.score}", align=("center"), font=('courier', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"game over :(", align='center', font=('courier', 20, 'normal'))

    def Score_generator(self):
        self.score += 100
        self.clear()
        self.write(arg=f"Score: {self.score}", align='center', font=('courier', 20, 'normal'))
