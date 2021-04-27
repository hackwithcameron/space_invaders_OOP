import pygame
import os
from levels import HEIGHT
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

    def move_lasers(self, speed, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def move(self, window_width, window_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:  # Move Left
            self.x -= self.player_speed
        if keys[pygame.K_d] and self.x + self.get_width() < window_width:  # Move Right
            self.x += self.player_speed
        if keys[pygame.K_w] and self.y > 0:  # Move Up
            self.y -= self.player_speed
        if keys[pygame.K_s] and self.y + self.get_height() + self.player_speed < window_height:  # Move Down
            self.y += self.player_speed
        if keys[pygame.K_SPACE]:
            self.shoot()
