import pygame


class Controller:
    def __init__(self, player_speed, player):
        self.keys = pygame.key.get_pressed()
        self.player_speed = player_speed
        self.player = player

    def get_input(self, player):
        if self.keys[pygame.K_a]:
            player.x -= self.player_speed
        if self.keys[pygame.K_d]:
            player.x += self.player_speed
        if self.keys[pygame.K_w]:
            player.y -= self.player_speed
        if self.keys[pygame.K_s]:
            player.y += self.player_speed
