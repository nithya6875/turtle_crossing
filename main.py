import time
from turtle import Screen
from scoreboard import Scoreboard
from cars import Cars
from crosser import Crosser

screen = Screen()
screen.setup(width=500, height=400)
turtle = Crosser()
screen.listen()
screen.tracer(0)


screen.onkeypress(fun=turtle.move_forward, key="Up")

game_is_on = True
cars = Cars()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect collision
    for blocks in cars.cars:
        if turtle.distance(blocks) < 20:
            scoreboard.game_over()
            game_is_on = False

        if turtle.won():
            scoreboard.increase_level()
            scoreboard.update_scoreboard()
            turtle.go_to_start()
            cars.increase_level()


screen.exitonclick()


