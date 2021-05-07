import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = list(range(-250, 250, 40))

class CarManager():
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        for x in range(0,6):
            self.add_car(x_cor=random.choice(list(range(-200,200))))

    def add_car(self, x_cor=300):
        x = Turtle(shape='square')
        x.shape('square')
        x.shapesize(stretch_wid=1, stretch_len=2)
        x.color(random.choice(COLORS))
        x.penup()
        x.goto(x=x_cor, y=random.choice(Y_POSITIONS))
        self.cars.append(x)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

            if(car.xcor()<-340):
                self.cars.remove(car)

    def level_up(self):
        self.speed+=MOVE_INCREMENT