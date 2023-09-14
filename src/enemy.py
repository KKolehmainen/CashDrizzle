from pathlib import Path
from random import randint, choice
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, velocity: int):
        super().__init__()
        self.width = width
        self.height = height
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "monster.png")
        self.image = pygame.transform.rotozoom(self.image,0,3.5)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.right = randint(self.image.get_width(), self.width)
        self.velocity = velocity
        self.direction = choice([-1, 1])

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.bottom >= self.height-int(10*6.4):
            self.rect.bottom = self.height-int(10*6.4)
            self.move(self.direction * self.velocity / 2)
    
    def move(self, velocity: int):
        self.rect.x += velocity
        if self.rect.right <= 0 or self.rect.left >= self.width:
            self.kill()

    def update(self):
        self.fall()