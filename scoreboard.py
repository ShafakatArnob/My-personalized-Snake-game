import turtle as t
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_sb()

    def update_sb(self):
        self.write(f"You can eat the poison only 2 times!\n"
                   f"             Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("YOU SUCK!", align=ALIGNMENT, font=FONT)

    def increase_sb(self):
        self.score += 1
        self.clear()
        self.update_sb()

    def decrease_sb(self):
        self.score -= 1
        self.clear()
        self.update_sb()

