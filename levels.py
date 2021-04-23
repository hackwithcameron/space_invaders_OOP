import pygame
import os

# Width and Height of the level
WIDTH, HEIGHT = 700, 700

# Load BG Image
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

