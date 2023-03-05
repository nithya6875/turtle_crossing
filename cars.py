from turtle import Turtle
import random

COLOURS = ["blue", "green", "yellow", "red", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        k = random.randint(1, 6)
        if k == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLOURS))
            new_car.penup()
            new_car.goto(240, random.randint(-170, 180))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
