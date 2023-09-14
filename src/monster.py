from pathlib import Path
from random import randint, choice
import pygame

class Hirvio(pygame.sprite.Sprite):
    def __init__(self, leveys: int, korkeus: int, nopeus: int):
        super().__init__()
        self.leveys = leveys
        self.korkeus = korkeus
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "monster.png")
        self.image = pygame.transform.rotozoom(self.image,0,3.5)
        self.rect = self.image.get_rect()
        self.rect.bottom = 0
        self.rect.right = randint(self.image.get_width(), self.leveys)
        self.nopeus = nopeus
        self.suunta = choice([-1, 1])

    def putoa(self):
        self.rect.y += self.nopeus
        if self.rect.bottom >= self.korkeus-int(10*6.4):
            self.rect.bottom = self.korkeus-int(10*6.4)
            self.liiku(self.suunta * self.nopeus / 2)
    
    def liiku(self, nopeus: int):
        self.rect.x += nopeus
        if self.rect.right <= 0 or self.rect.left >= self.leveys:
            self.kill()

    def update(self):
        self.putoa()