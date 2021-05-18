import random
from turtle import Turtle, Screen

# UI creation
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('grey')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []


def get_user_bet():
    """
    Asks the user for a color and checks to make sure the color is in the list of options
    :return: string of color name
    """
    bet_color = None
    while bet_color not in colors:
        bet_color = screen.textinput(title="Make your bet",
                                     prompt="Which turtle will win the race? Enter a color: ").lower()
    return bet_color


# I wanted a drop down menu for the color selection, but it seemed not to be possible within turtle itself
user_bet = get_user_bet()

# Sets up game
y_cor = -125
for item in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(item)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor)
    y_cor += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# Game logic
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'Sorry, the {winning_color} turtle won the race. Better luck next time.')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
