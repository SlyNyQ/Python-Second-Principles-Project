import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")

# def get_mouse_click_colour(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_colour)
#
# turtle.mainloop()

#TODO: Keep track of the score
correct_guesses = 0

data = pandas.read_csv("50_states.csv")
states = data["state"]
x_cord = data["x"]
y_cord = data["y"]

#TODO: Record the correct guesses in a list
guessed_state = []

#TODO: Use a loop to allow the user to keep guessing
while correct_guesses < 50:
    #TODO: Convert the guess to title case
    answer_state = screen.textinput(title="Guess the state", prompt = f"{correct_guesses}/50 States Correct")
    print(answer_state)

    if answer_state is None:
        break

    answer_state = answer_state.strip().title()

    #TODO: Check if the guess is correct among the 50 states
    if answer_state in states.values and answer_state not in guessed_state:

        correct_guesses += 1
        guessed_state.append(answer_state)
        print("Correct")

        correct_state = data[states == answer_state]
        #TODO: Write correct guesses on the map
        x = correct_state.iloc[0]["x"]
        y = correct_state.iloc[0]["y"]


        writer.goto(x, y)

        writer.write(answer_state)







screen.exitonclick()