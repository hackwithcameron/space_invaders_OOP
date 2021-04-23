import pygame
import os
from controller import Controller
from ship import Ship

PLAYER_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
PLAYER_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_SHIP
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.player_speed = 5
