#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from foo import Draw, Check, Cursor, Desk


from time import sleep
#initialization ev3

ev3 = EV3Brick()

#initialization field

symbol = ["x", "o"]

field = [
    ["c1", "c2", "c3"],
    ["b1", "b2", "b3"],
    ["a1", "a2", "a3"] ]


    #initialization field
#Draw("field").draw()

desk = Desk()
desk.draw_desk()
    #start game

i = 0
cur = Cursor(field, symbol, i)
desk.set_xy(1,1)
while Check(field).check() == False:
    desk.draw_circle()
    
    if Button.RIGHT in ev3.buttons.pressed():
        cur.move('right')
    if Button.LEFT in ev3.buttons.pressed():
        cur.move('left')
    if Button.UP in ev3.buttons.pressed():
        cur.move('up')
    if Button.DOWN in ev3.buttons.pressed():
        cur.move('down')
    if Button.CENTER in ev3.buttons.pressed():
        pass
    cur.draw()
    if i != 0:
        i = 0
    else:
        i = 1




