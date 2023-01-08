import random
import pygame

class Enemy:
    def __init__(self, game):
        self.game = game
        self.color = (0, 100, 0)
        self.size = (20, 20)
        self.pos = (random.randint(0, self.game.window_size[0]), random.randint(0, self.game.window_size[1]))

    def collides_with(self, player):
        return pygame.Rect(self.pos, self.size).colliderect(player.pos, (player.radius*2, player.radius*2))

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.pos, self.size))
