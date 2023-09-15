import unittest
from player import Player
import pygame

class Testplayer(unittest.TestCase):
    def test_player_cannot_go_left_of_screen(self):
        player = Player(640, 480)
        player.move_left(1000)

        self.assertGreaterEqual(player.rect.left, 0)

    def test_player_cannot_go_right_of_screen(self):
        player = Player(640, 480)
        player.move_right(1000)

        self.assertLessEqual(player.rect.right, 640)

    def test_player_does_not_fall_through_ground(self):
        player = Player(640, 480)
        place_on_ground = player.rect.bottom
        player.fall()

        self.assertEqual(player.rect.bottom, place_on_ground)

    def test_player_jumps(self):
        player = Player(640, 480)
        place_on_ground = player.rect.bottom
        player.jump()
        player.fall()

        self.assertLess(player.rect.bottom, place_on_ground)

    def test_player_cannot_jump_in_air(self):
        player = Player(640, 480)
        player.jump()
        player.fall()
        player.jump()

        self.assertEqual(player.gravity, -19)