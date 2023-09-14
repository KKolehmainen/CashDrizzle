from pathlib import Path
from random import randint
import pygame

class Kolikko(pygame.sprite.Sprite):
    def __init__(self, leveys: int, korkeus: int, nopeus: int):
        super().__init__()
        self.leveys = leveys
        self.korkeus = korkeus
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "coin.png")
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.right = randint(self.image.get_width(), self.leveys)
        self.nopeus = nopeus

    def putoa(self):
        self.rect.y += self.nopeus
        if self.rect.top >= self.korkeus:
            self.kill()

    def update(self):
        self.putoa()