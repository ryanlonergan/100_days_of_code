import pandas as pd
import turtle

from writer import Writer

# Initial UI creation
screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(750, 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Creating lists for game logic
states = pd.read_csv('50_states.csv')
state_list = states.state.tolist()
guesses = []

writer = Writer()

# Game logic
while len(guesses) < 50:
    answer_state = screen.textinput(title=f'{len(guesses)}/50 States Correct',
                                    prompt='What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        break
    if answer_state in state_list:
        current_state = (states[states.state == answer_state])
        if current_state.state.item() not in guesses:
            writer.correct_guess(current_state)
            guesses.append(current_state.state.item())

# Creating a .csv of states that the user was unable to guess
states_to_learn = [state for state in state_list if state not in guesses]
df = pd.DataFrame(states_to_learn, columns=['state_name'])
df.to_csv('states_to_learn.csv', index=False)
