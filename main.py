import random
from turtle import Turtle, Screen


def winner_check(color_of_winner, user_choice):
    return color_of_winner == user_choice


is_race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
colors = ["red", "green", "yellow", "orange", "pink", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race enter a color: ")
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        turtle_position = turtle.xcor()
        if turtle_position >= 230 and winner_check(color_of_winner=turtle.pencolor(), user_choice=user_input):
            print()
            print(f"You won! The winner is {turtle.pencolor()}")
            is_race_on = False
            break
        elif turtle_position >= 230 and not winner_check(color_of_winner=turtle.pencolor(), user_choice=user_input):
            print()
            print(f"You lose. The winner is {turtle.pencolor()}")
            is_race_on = False
            break
screen.exitonclick()

# def move_forward():
#     tim.fd(10)
#
#
# def move_back():
#     tim.back(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def clear():
#     tim.home()
#     tim.clear()
#
#
# screen.listen()
# screen.onkeypress(move_forward, "w")
# screen.onkeypress(move_back, "s")
# screen.onkeypress(turn_left, "a")
# screen.onkeypress(turn_right, "d")
# screen.onkey(clear, "c")
# screen.mainloop()
