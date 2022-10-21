#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
#initialization ev3

ev3 = EV3Brick()

field = [
    [[59, 0],  [59, 128] ],
    [[118, 0], [118, 128]],
    [[0, 85],  [178, 85] ],
    [[0, 42],  [178, 42] ],
]

o    = [28, 107, 21]

X    = [
    [[1, 128], [59, 83]],
    [[59, 128], [1, 83]]
]


class Draw:
    def __init__(self, sort: str, cell_x=0, cell_y=0):
    
        self.sort   = sort
        self.cell_x = cell_x
        self.cell_y = cell_y 

        self.kx =  59
        self.ky =  43
    def get_real_x (self):
        return self.cell_x *self.kx

    def get_real_y (self):
        return self.cell_y *self.ky

    def draw(self):
        if self.sort == "field":
            x     = 0
            y     = 0
            count = 0

            while count < 4:

                x1 = field[count][y][x]
                y1 = field[count][y][x+1]
                x2 = field[count][y+1][x]
                y2 = field[count][y+1][x+1]

                ev3.screen.draw_line(x1, y1, x2, y2)

                count+=1
        
        if self.sort == "o":

            ev3.screen.draw_circle(o[0] + self.get_real_x, o[1] - self.cell_y, o[2])

        if self.sort == "x":
            
            ev3.screen.draw_line(X[0][0][0] + self.cell_x, X[0][0][1] - self.cell_y, X[0][1][0] + self.cell_x, X[0][1][1] - self.cell_y)
            ev3.screen.draw_line(X[1][0][0] + self.cell_x, X[1][0][1] - self.cell_y, X[1][1][0] + self.cell_x, X[1][1][1] - self.cell_y)

class Desk:
    def __init__(self):
        self.field = [
        [[59, 0],  [59, 128] ],
        [[118, 0], [118, 128]],
        [[0, 85],  [178, 85] ],
        [[0, 42],  [178, 42] ],
        ]

        self.cell_x = 0
        self.cell_y = 0 

        self.kx =  59
        self.ky =  43

    def draw_desk(self):
        x = 0
        y = 0
        count = 0
        while count < 4:

            x1 = self.field[count][y][x]
            y1 = self.field[count][y][x+1]
            x2 = self.field[count][y+1][x]
            y2 = self.field[count][y+1][x+1]

            ev3.screen.draw_line(x1, y1, x2, y2)

            count+=1  

    def get_real_x (self):
        return self.cell_x *self.kx

    def get_real_y (self):
        return self.cell_y *self.ky
    
    def set_xy(self, x, y):
        self.cell_x = x
        self.cell_y = y 

    def draw_circle(self):
        
        ev3.screen.draw_circle(o[0] + self.get_real_x(), o[1] - self.get_real_y(), o[2])


class Check:
    def __init__(self, field: list=None):
        self.field = field

    def check(self):
        if field:
            return False


class Cursor:
    def __init__(self, field: list, symb: list, i: int = 1):
        self.field = field
        self.symb  = symb
        self.i     = i
        
        self.x = 33
        self.y = 29

        self.circle_x = 0
        self.circle_y = 0

        self.dx = 59
        self.dy = 43

        #i = self.i

        x1 = 0
        y1 = 0
        """
        if (y <= 128 and y >= 0) and (x <= 178 and x >= 0):

            if Button.LEFT in ev3.buttons.pressed():
                x -= 59
                x1 -= 1
                if (y <= 128 and y >= 0) and (x <= 178 and x >= 0):
                    ev3.screen.draw_circle(o[0] + x, o[1] - y, o[2])

            if Button.RIGHT in ev3.buttons.pressed():
                x += 59
                x1 += 1
                if (y <= 128 and y >= 0) and (x <= 178 and x >= 0):
                    ev3.screen.draw_circle(o[0] + x, o[1] - y, o[2])

            if Button.UP in ev3.buttons.pressed():
                y -= 43
                y1 -= 1
                if (y <= 128 and y >= 0) and (x <= 178 and x >= 0):
                    ev3.screen.draw_circle(o[0] + x, o[1] - y, o[2])

            if Button.DOWN in ev3.buttons.pressed():
                y += 43
                y1 += 1
                if (y <= 128 and y >= 0) and (x <= 178 and x >= 0):
                    ev3.screen.draw_circle(o[0] + x, o[1] - y, o[2])
                
            if Button.CENTER in ev3.buttons.pressed():
                if not "o" and not "x" in self.field[y1][x1]:
                    Draw(self.move[i], x, y).draw() 

        return self.field[y1][x1] + self.move[i]
"""


    def draw(self):
        ev3.screen.draw_circle(self.x, self.y, 3, fill=True)
    def clear(self):
        ev3.screen.draw_circle(self.x, self.y, 3, fill=True, color=Color.WHITE)
    def move(self, deistv):
        if deistv == 'left':

            self.clear()
            self.x -= self.dx
            self.i -= 1
            sleep(0.7)

        elif deistv =='right':
            
            self.clear()
            self.x += self.dx
            self.i += 1
            print(self.x)
            sleep(0.7)

        elif deistv =='up':
            self.clear()
            self.y -= self.dy
            self.i -= 3
            sleep(0.7)

        elif deistv =='down':
            self.clear()
            self.y += self.dy
            self.i += 3
            sleep(0.7)

    def get_pos(self):
        return self.i 
