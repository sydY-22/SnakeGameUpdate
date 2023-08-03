from turtle import Turtle
ALIGNMENT = "right"
FONT = ("Impact", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(250,260)
        self.pencolor('white')
        self.show_score()

    def show_score(self):
        """Displays the Score."""
        self.clear()
        with open("data.txt", mode="r") as file:
            contents = file.read()
        self.write(f"Score: {self.score} | High Score: {contents}", align=ALIGNMENT, font=FONT)

    def reset_highscore(self):
        """Changes to a new highscore when reached."""
        with open("data.txt", mode="r") as file:
            contents = file.read()
        if self.score > int(contents):
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.show_score()

    def game_over(self):
        """Displays game over if the player dies."""
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER!", align="center", font=FONT)

    def add_score(self):
        """Adds to the Scoreboard."""
        self.score += 1
        self.show_score()

