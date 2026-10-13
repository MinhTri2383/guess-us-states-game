import turtle
from pathlib import Path

import pandas

BASE_DIR = Path(__file__).resolve().parent

FONT = ("Courier", 10, "normal")
WIN_FONT = ("Courier", 50, "normal")

# TURTLE
screen = turtle.Screen()
screen.title("U.S. States game")
image = str(BASE_DIR / "blank_states.gif")
screen.addshape(image)
turtle.shape(image)

write_on_map = turtle.Turtle()
write_on_map.penup()
write_on_map.hideturtle()

# PANDAS
file = "50_states.csv"
data = pandas.read_csv(BASE_DIR/ file)
all_states = data.state.to_list()
guessed_states = []

play = True
while play:
    
    # Turtle
    screen.update()
    answer = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="Enter a state's name, or type Quit to exit: ",
    )

    if answer is None or answer.strip().lower() == "quit":
        learning_states = [
            state for state in all_states
            if state not in guessed_states
        ]

        pandas.DataFrame({"State": learning_states}).to_csv(
            BASE_DIR / "states-to-learn.csv",
            index=False,
        )
        break

    answer_state = answer.strip().title()

    # Pandas
    if answer_state in all_states and answer_state not in guessed_states:
        print(answer_state)
        guessed_states.append(answer_state)

        # Turtle
        state_row = data.loc[data["state"] == answer_state].iloc[0]
        write_on_map.goto(x=int(state_row["x"]), y=int(state_row["y"]))
        write_on_map.write(arg=answer_state, align="center", font=FONT)

    if len(guessed_states) == 50 and play:
        write_on_map.goto(x= 0, y= 200)
        write_on_map.color("Red")
        write_on_map.write(arg="YOU WIN!", align="center", font=WIN_FONT)
        play = False
        screen.exitonclick()