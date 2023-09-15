import unittest
from enemy import Enemy
import pygame

class TestEnemy(unittest.TestCase):
    def test_enemy_falls_with_correct_velocity(self):
        enemy = Enemy(640, 480, 5)
        enemy.update()

        self.assertEqual(enemy.rect.bottom, 5)

    def test_enemy_is_removed_outside_screen(self):
        enemy = Enemy(640, 480, 5000)
        group = pygame.sprite.Group()
        group.add(enemy)
        enemy.update()
        
        self.assertFalse(enemy.alive())

    def test_enemy_does_not_fall_through_ground(self):
        enemy = Enemy(640, 480, 500)
        group = pygame.sprite.Group()
        group.add(enemy)
        enemy.update()

        self.assertLessEqual(enemy.rect.bottom, 499)