from turtle import Turtle , Screen
import random
import turtle

colors = ["red", "blue", "green", "orange", "yellow", "purple"]
is_race_on = False

#Screen
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet!", prompt="Which turtle will win in the race? Enter a color : ")

#create turtles
all_turtles = []
for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(165 - (x*65)))
    all_turtles.append(new_turtle)

#Race
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else: 
                print("You lose!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

#exit
screen.exitonclick()