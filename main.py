import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    loop_count+=1
    screen.update()
    car_manager.move_cars()

    if(loop_count%6==0):
    	car_manager.add_car()

    for car in car_manager.cars:
    	if(car.distance(player)<20):
    		game_is_on = False
    		break

    if(player.has_crossed()):
    	player.go_to_start()
    	car_manager.level_up()
screen.exitonclick()