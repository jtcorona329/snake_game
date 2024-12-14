from turtle import Turtle
ALIGN = "center"
FONT = "Arial"
FONT_SIZE = 20
FONT_STYLE = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt", "r") as f:
            self.high_score = int(f.read())
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as f:
            f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", False, align=ALIGN, font=(FONT, FONT_SIZE, FONT_STYLE))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=(FONT, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


