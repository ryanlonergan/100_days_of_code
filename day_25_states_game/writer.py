from turtle import Turtle

FONT = ("Arial", 8, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def correct_guess(self, current_state):
        """
        Writes the state name to the map

        :param current_state:  name of state that user guessed correctly
        """
        state_name = str(current_state.state.item())
        x = int(current_state.x.item())
        y = int(current_state.y.item())
        self.goto(x, y)
        self.write(f'{state_name}', align='center', font=FONT)
