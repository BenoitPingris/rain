#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## arcade
## File description:
## main
##

"""
'Rain' simulator
"""

import sys
import arcade
import random

def translate(value, l_min, l_max, r_min, r_max):
    a = l_max - l_min
    b = r_max - r_min

    new_value = float(value - l_min) / float(a)
    return r_min + (new_value * b)


class Rain:
    def __init__(self):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(HEIGHT + 100, HEIGHT + 500)
        self.w = random.randrange(1, 2)
        self.h = 20
        self.color = (30, 20, 200)
        self.g = 2
        self.speed = random.uniform(0.02, 0.1)
#        self.speed = translate(self.w, 1, 4, 0.04, 0.05)


    def update(self):
        self.g += self.speed
        self.y -= self.g
        if self.y <= 0:
            self.y = random.randrange(HEIGHT + 100, HEIGHT + 500)
            self.x = random.randrange(0, WIDTH)
            self.g = 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "floating")
        self.rains = []
        for i in range(500):
            self.rains.append(Rain())


    def on_draw(self):
        arcade.start_render()
        for rain in self.rains:
            arcade.draw_rectangle_filled(rain.x, rain.y, rain.w, rain.h, rain.color)


    def update(self, delta_time):
        for rain in self.rains:
            rain.update()


def main():
    """
    Main function
    """
    game = Game()
    arcade.run()
    return SUCCESS


if __name__ == '__main__':
    SUCCESS = 0
    ERROR = 84
    WIDTH = 600
    HEIGHT = 600
    sys.exit(main())
