#importing main components
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#variables
 
draw_x_coordinates = #
draw_o_coordinates = #some function...

#classes

class Draw:
    def __init__(draw_type: str, x_coordinate: int, y_coordinate: int):

        self.draw_type    = draw_type
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def
