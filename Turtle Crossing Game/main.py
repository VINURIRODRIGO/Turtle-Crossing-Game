import time
from player import Player
from turtle import Screen
from racetracks import RacingTracks
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
racing_track = RacingTracks()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_forward, key="Up")
current_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(current_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.moving_cars()
    for cars in car_manager.car_direction:
        if cars.distance(player) < 28:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        scoreboard.new_level()
        player.goto_start()
        current_speed *= 0.5
        print(current_speed)

screen.exitonclick()
