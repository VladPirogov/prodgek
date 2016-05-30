import unittest
from .prodgek import game
import pygame

pygame.init()
screen = pygame.display.set_mode([400, 400])

class prodgekTestCase(unittest.TestCase):

    def test_You_go_left(self):
        player = You()
        start_x = player.rect.x
        player.left()
        new_x = player.rect.x
        expected_x = start_x - 10
        self.assertEqual(new_x, expected_x)

    def test_You_go_right(self):
        player = You()
        start_x = player.rect.x
        cat.right()
        new_x = player.rect.x
        expected_x = start_x + 10
        self.assertEqual(new_x, expected_x)



if __name__ == '__main__':
    unittest.main()
