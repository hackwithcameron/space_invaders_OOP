import pygame
from collision_detection import collide


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def off_screen(self, height):
        return height <= self.y <= 0

    def collision(self, obj):
        return collide(obj, self)
