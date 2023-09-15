from pathlib import Path
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        graphics_path = Path(__file__).parents[1] / "graphics"
        self.image = pygame.image.load(graphics_path / "robo.png")
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect(midbottom=(width / 2, height-int(10*6.4)))
        self.velocity = 10
        self.gravity = 0
    
    def events(self):
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_RIGHT] and self.rect.right <= self.width:
            self.move_right(self.velocity)
        if buttons[pygame.K_LEFT] and self.rect.left >= 0:
            self.move_left(self.velocity)
        if buttons[pygame.K_SPACE] and self.rect.bottom >= self.height-int(10*6.4):
            self.jump()

    def move_right(self, velocity: int):
        self.rect.x += velocity

    def move_left(self, velocity: int):
        self.rect.x -= velocity

    def jump(self):
        self.gravity = -20

    def fall(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.height-int(10*6.4):
            self.rect.bottom = self.height-int(10*6.4)

    def update(self):
        self.events()
        self.fall()