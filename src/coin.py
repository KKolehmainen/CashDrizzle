from pathlib import Path
from random import randint
import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, velocity: int):
        super().__init__()
        self.width = width
        self.height = height
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "coin.png")
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.right = randint(self.image.get_width(), self.width)
        self.velocity = velocity

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top >= self.height:
            self.kill()
