import pygame

class Player:
    def __init__(self, game):
        self.game = game
        self.color = (0, 0, 0)
        self.pos = (200, 200)
        self.radius = 20

    def update(self, keys):
        if keys[pygame.K_w]:
            self.pos = (self.pos[0], self.pos[1] - 1)
        if keys[pygame.K_s]:
            self.pos = (self.pos[0], self.pos[1] + 1)
        if keys[pygame.K_a]:
            self.pos = (self.pos[0] - 1, self.pos[1])
        if keys[pygame.K_d]:
            self.pos = (self.pos[0] + 1, self.pos[1])

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, self.pos, self.radius)
