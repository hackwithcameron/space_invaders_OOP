import pygame
import random
import time

import levels
from player import Player
from enemy import Enemy

pygame.font.init()
pygame.display.set_caption("Space Invaders")


class Game:
    def __init__(self):
        self.WIN = pygame.display.set_mode((levels.WIDTH, levels.HEIGHT))

        self.play = True
        self.lost = False
        self.FPS = 60
        self.level = 0
        self.wave = 0
        self.lives = 5
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.lost_font = pygame.font.SysFont("comicsans", 50)

        self.clock = pygame.time.Clock()

        # Create Player using x, y coordinates
        self.player = Player(300, 600)
        self.enemies = []

        self.laser_speed = 10

    # Main drawing method
    def update_window(self):
        self.WIN.blit(levels.BG, (0, 0))
        lives_label = self.main_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        levels_label = self.main_font.render(f"Level: {self.level}", True, (255, 255, 255))

        self.WIN.blit(lives_label, (10, 10))
        self.WIN.blit(levels_label, (levels.WIDTH - levels_label.get_width() - 10, 10))
        # Draws enemies and player
        for enemy in self.enemies:
            enemy.draw(self.WIN)
        self.player.draw(self.WIN)

        if self.lost:
            lost_label = self.lost_font.render("You Lost!!!", True, (255, 255, 255))
            self.WIN.blit(lost_label, (levels.WIDTH/2 - lost_label.get_width()/2, levels.HEIGHT/2 - lost_label.get_height()))

        pygame.display.update()

    def run(self):
        while self.play:
            self.clock.tick(self.FPS)
            if self.lives <= 0:
                self.lost = True
            # Creates list of enemies. Advances level if no enemies exist
            if len(self.enemies) == 0:
                self.level += 1
                self.wave += 5
                for i in range(self.wave):
                    enemy = Enemy(random.randrange(5, levels.WIDTH - 100), random.randrange(-2500, -100),
                                  random.choice(["red", "blue", "green"]))
                    self.enemies.append(enemy)

            # Updates window
            self.update_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            self.player.move_lasers(-self.laser_speed, self.enemies)
            self.player.move(levels.WIDTH, levels.HEIGHT)

            for enemy in self.enemies[:]:
                enemy.move()
                enemy.move_lasers(self.laser_speed, self.player)
                # Checks to see if enemy ship has reached bottom of game window and removes enemy from list and one life
                if enemy.get_height() + enemy.y > levels.HEIGHT:
                    self.lives -= 1
                    self.enemies.remove(enemy)
