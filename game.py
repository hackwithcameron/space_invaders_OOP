import pygame
import os
import time

import levels
from player import Player

pygame.font.init()
pygame.display.set_caption("Space Invaders")

RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))


class Game:
    def __init__(self):
        self.WIN = pygame.display.set_mode((levels.WIDTH, levels.HEIGHT))

        self.play = True
        self.FPS = 60
        self.level = 1
        self.lives = 5
        self.main_font = pygame.font.SysFont("comicsans", 50)

        self.clock = pygame.time.Clock()

        # Create Player
        self.player = Player(300, 600)

    def update_window(self):
        self.WIN.blit(levels.BG, (0, 0))
        lives_label = self.main_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        levels_label = self.main_font.render(f"Level: {self.level}", True, (255, 255, 255))

        self.WIN.blit(lives_label, (10, 10))
        self.WIN.blit(levels_label, (levels.WIDTH - levels_label.get_width() - 10, 10))
        self.player.draw(self.WIN)

        pygame.display.update()

    def run(self):
        while self.play:
            self.clock.tick(self.FPS)
            self.update_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
