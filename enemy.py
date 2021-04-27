import pygame
import os

from laser import Laser
from ship import Ship


class Enemy(Ship):
    RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
    BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
    GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

    RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
    BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
    GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

    SHIP_MAP = {
        "red": (RED_SHIP, RED_LASER),
        "blue": (BLUE_SHIP, BLUE_LASER),
        "green": (GREEN_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.SHIP_MAP[color]
        self.speed = 2
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        self.y += self.speed

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


