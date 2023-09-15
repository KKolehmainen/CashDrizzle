import unittest
from coin import Coin
import pygame

class TestCoin(unittest.TestCase):
    def test_coin_falls_with_correct_velocity(self):
        coin = Coin(640, 480, 5)
        coin.update()

        self.assertEqual(coin.rect.bottom, 5)

    def test_coin_is_removed_outside_screen(self):
        coin = Coin(640, 480, 1000)
        group = pygame.sprite.Group()
        group.add(coin)
        coin.update()
        
        self.assertFalse(coin.alive())

        