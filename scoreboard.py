from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as HS:
            hs = HS.read()
        self.high_score = int(hs)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Courier", 20, "normal"))
        self.hideturtle()
        print(type(self.high_score))
        # self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_scoreboard()
            with open("data.txt", mode="w") as HS:
                HS.write(f"{(self.high_score)}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center",font=("Arial", 24, "normal"))

