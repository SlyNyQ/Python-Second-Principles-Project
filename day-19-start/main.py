from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width =500, height = 400)
user_bet = screen.textinput(title = "Make your Bets!!", prompt ="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#tim = Turtle(shape = "turtle")
tims = [Turtle(shape = "turtle") for _ in range(6)]
# tim.penup
yo = -100
for i,tim in enumerate(tims):
    tim.penup()
    tim.color(colors[i%6])
    tim.goto(x=-230,y=yo)
    yo += 30

if user_bet:
    is_race_on = True

while is_race_on == True:

    for tim in tims:
        if tim.xcor() > 230:
            is_race_on = False
            winning_colour = tim.pencolor()
            if winning_colour == user_bet:
                print(f"You won the race! The {winning_colour} turtle wins!")

            else:
                print(f"You Lost! The {winning_colour} turtle wins!")

        random_distance = random.randint(0, 10)
        tim.forward(random_distance)

screen.exitonclick()