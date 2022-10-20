#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from resourses import Draw

#initialization ev3

ev3 = EV3Brick()

#initialization field
field = [
    ["a1o", "a2", "a3x"],
    ["b1", "b2o", "b3"],
    ["c1x", "c2", "c3"]
]

while True:

    field = 

    draw = Draw("field")
