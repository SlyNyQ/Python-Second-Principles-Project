import turtle
from turtle import *
import random as rnd

tim = Turtle()
turtle.colormode(255)


tim.shape("turtle")
#tim.color("aquamarine3")
tim.color("DarkOrchid")
colour = [
    "royal blue",
    "aquamarine3",
    "DarkOrchid",
    "sienna",
    "green",
    "crimson",
    "yellow",
    "MidnightBlue",
    "IndianRed",
    "SlateGray",
]

def random_color():
    r = rnd.randint(0,255)
    g = rnd.randint(0,255)
    b = rnd.randint(0,255)
    random_colour = (r,g,b)
    return random_colour
directions = [lambda: tim.rt(90), lambda: tim.lt(90)]

movements = [
    lambda: tim.forward(30),
    lambda: tim.backward(30),
]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(10)
        tim.right(angle)

def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)

def draw_triangle():
    for _ in range(6):
        tim.forward(80)
        tim.left(60)

def random_walk(length_of_walk):
    """Does random walk for turtle object"""
    for _ in range(length_of_walk):
        chosen_direction = rnd.choice(directions)
        chosen_direction()
        chosen_move = rnd.choice(movements)
        chosen_move()

def draw_spirograph(size_of_gap):
    """Draws spirograph for turtle object"""
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.speed("fastest")
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# for shape_side_n in range(3,40):
#     tim.color(rnd.choice(colour))
#     tim.speed("fastest")
#     draw_shape(shape_side_n)
dirs = [0,90,180,270]
# for walk_length in range(30):
#     #tim.color(rnd.choice(colour))
#     tim.color(random_color())
#     tim.width(5)
#     tim.speed("fastest")
#     tim.setheading(rnd.choice(dirs))
#     random_walk(walk_length)
heading = 0
# for run in range(100):
#     #tim.color(random_color())
#     tim.speed("fastest")
#     tim.setheading(heading)
#     tim.circle(100)
#     tim.circle(50)
#     #tim.color(random_color())
#     draw_square()
#     #tim.color(random_color())
#     draw_triangle()
#
#     heading +=10
draw_spirograph(1)
# for _ in range(100):
#     # tim.color(rnd.choice(colour))
#     tim.color(random_color())
#     tim.width(10)
#     tim.speed("fastest")
#     tim.forward(30)
#     tim.setheading(rnd.choice(dirs))

# move_count = 0
# for i in range(19):
#     tim.forward(100)
#     if move_count < 3:
#         tim.right(120)
#     elif move_count < 7:
#         tim.color("yellow")
#         tim.right(90)
#     elif move_count < 12:
#         tim.color("red")
#         tim.right(72)
#     elif move_count < 18:
#         tim.color("green")
#         tim.right(60)
#     move_count += 1

import heroes
print(heroes.gen())



























screen = Screen()
screen.exitonclick()