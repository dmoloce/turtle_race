import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Turtle racing", prompt="Which turle will win the race? Choose a color")

colors = ['red', 'blue', 'pink','green', 'orange', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for index in range(0, 6):
    new_turle = Turtle(shape="turtle")
    new_turle.color(colors[index])
    new_turle.penup()
    new_turle.goto(x = -230, y = y_position[index])
    all_turtles.append(new_turle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == bet:
                print(f"You've won! The {winner} turle is the winner!" )
            else:
                print(f"You've lost! The {winner} turle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()