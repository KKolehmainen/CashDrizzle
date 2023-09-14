from pathlib import Path
from random import randint
import pygame

from player import Player
from coin import Coin
from enemy import Enemy

class CashDrizzle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Cash Drizzle")
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        graphics_path = Path(__file__).parents[1] / "graphics"
        font_file = graphics_path / "PressStart2P-vaV7.ttf"
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.width, self.height))
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.font = pygame.font.Font(font_file, 30)
        self.small_font = pygame.font.Font(font_file, 13)
        self.game_on = False
        self.start_menu = True
        self.points = 0
        self.sky = pygame.image.load(graphics_path / "sky.png")
        self.sky = pygame.transform.scale(self.sky, (640,int(100*6.4)))
        self.ground = pygame.image.load(graphics_path / "ground.png")
        self.ground = pygame.transform.scale(self.ground, (640,int(15*6.4)))
        self.loop()

    def loop(self):
        while True:
            self.handle_exit()

            if self.start_menu:
                self.draw_start_menu()
                self.select()
            elif self.game_on:
                self.add_coin()
                self.add_enemy()
                self.player.update()
                self.coins.update()
                self.enemies.update()
                if self.collide(self.coins):
                    self.points += 1
                if self.collide(self.enemies):
                    self.game_on = False
                self.draw_screen()
            else:
                self.draw_menu()
                self.select()
            self.clock.tick(60)

    def handle_exit(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
    
    def add_coin(self):
        if randint(1,100) < 3:
            self.coins.add(Coin(self.width, self.height, 5))

    def add_enemy(self):
        if randint(1,1000) < 5:
            self.enemies.add(Enemy(self.width, self.height, 5))

    def collide(self, group):
        if pygame.sprite.spritecollide(self.player.sprite, group, True, 
                pygame.sprite.collide_mask):
            return True
        else:
            return False

    def draw_screen(self):
        self.screen.blit(self.sky, (0,0))
        self.screen.blit(self.ground, (0,self.height-self.ground.get_height()))
        self.player.draw(self.screen)
        self.coins.draw(self.screen)
        self.enemies.draw(self.screen)
        points = self.small_font.render(f"Points: {self.points}", True, (0, 0, 240))
        self.screen.blit(points, (self.width - 180, 10))
        pygame.display.flip()

    def draw_start_menu(self):
        self.screen.fill((0, 0, 0))
        header = self.font.render("Cash Drizzle", True, (255, 0, 180))
        description = "Collect coins and dodge enemies."
        instruction = ["Commands:","Move left = left arrowkey",
                "Move right = right arrowkey", "Jump = spacebar"]
        self.screen.blit(header, ((self.width - header.get_width())/2, 50))
        desc_text = self.small_font.render(description, True, (255, 0, 180))
        self.screen.blit(desc_text, (100, 150))
        for i, line in enumerate(instruction):
            line_text = self.small_font.render(line, True, (255, 0, 180))
            self.screen.blit(line_text, (100, 200+24*i))
        start = self.small_font.render("Press enter to start!", True, (255, 0, 180))
        self.screen.blit(start, ((self.width - start.get_width())/2, 400))
        pygame.display.flip()
    
    def draw_menu(self):
        points = self.font.render(f"Points: {self.points}", True, (255, 0, 180))
        new_game = self.small_font.render("Press enter to start a new game!", True, (255, 0, 180))
        self.screen.blit(points, ((self.width - points.get_width())/2, 100))
        self.screen.blit(new_game, ((self.width - new_game.get_width())/2, 200))
        pygame.display.flip()

    def select(self):
        buttons = pygame.key.get_pressed()
        if buttons[pygame.K_RETURN]:
            self.game_on = True
            self.start_menu = False
            self.points = 0
            self.coins.empty()
            self.enemies.empty()
            self.player.empty()
            self.player.add(Player(self.width, self.height))

if __name__ == "__main__":
    CashDrizzle()
