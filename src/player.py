from pathlib import Path
import pygame

class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, leveys: int, korkeus: int):
        super().__init__()
        self.leveys = leveys
        self.korkeus = korkeus
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "robo.png")
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect(midbottom=(leveys / 2, korkeus-int(10*6.4)))
        self.nopeus = 10
        self.painovoima = 0
    
    def tapahtumat(self):
        napit = pygame.key.get_pressed()
        if napit[pygame.K_RIGHT] and self.rect.right <= self.leveys:
            self.rect.x += self.nopeus
        if napit[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.nopeus
        if napit[pygame.K_SPACE] and self.rect.bottom >= self.korkeus-int(10*6.4):
            self.painovoima = -20

    def putoa(self):
        self.painovoima += 1
        self.rect.y += self.painovoima
        if self.rect.bottom >= self.korkeus-int(10*6.4):
            self.rect.bottom = self.korkeus-int(10*6.4)

    def update(self):
        self.tapahtumat()
        self.putoa()