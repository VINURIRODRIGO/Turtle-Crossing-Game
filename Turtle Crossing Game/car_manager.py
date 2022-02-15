import random

from player import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_DIRECTION = [-200, -130, -60, 0, 80, 150, 215]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_direction = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random.shuffle(Y_DIRECTION)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.choice(Y_DIRECTION)
            new_car.goto(300, random_y)
            self.car_direction.append(new_car)

    def moving_cars(self):
        for cars in self.car_direction:
            cars.backward(MOVE_INCREMENT)
