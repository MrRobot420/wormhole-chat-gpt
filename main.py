import random
import pygame
from src.player import Player
from src.enemy import Enemy

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set the window size
        self.window_size = (800, 600)

        # Create the window
        self.screen = pygame.display.set_mode(self.window_size)

        # Set the title of the window
        pygame.display.set_caption('My Game')

        # Set the background color
        self.bg_color = (255, 255, 255)

        # Create the player object
        self.player = Player(self)

        # Create a list to store the enemy objects
        self.enemies = []

        # Create a font object
        self.font = pygame.font.Font(None, 36)

        # Initialize the score
        self.score = 0

        # Game loop
        self.running = True

    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Add new enemies to the list
            if len(self.enemies) < 20:
                self.enemies.append(Enemy(self))

            # Get the keys that are being pressed
            keys = pygame.key.get_pressed()

            # Update the player's position based on the keys that are being pressed
            self.player.update(keys)

            # Draw the background
            self.screen.fill(self.bg_color)

            # Draw the player
            self.player.draw()

            # Draw the enemies
            for enemy in self.enemies:
                enemy.draw()

                # Check if the player is colliding with the enemy
                if enemy.collides_with(self.player):
                    # Swallow the enemy
                    self.enemies.remove(enemy)

                    # Increase the player's size
                    self.player.radius += 5
                    self.score += 100

            # Check if the player has won
            if self.player.radius >= min(self.window_size) / 2:
                # Display end screen
                end_color = (100, 100, 100)
                self.screen.fill(end_color)
                end_text = self.font.render("You won!", True, (200, 100, 100))
                self.screen.blit(end_text, (self.window_size[0] / 2, self.window_size[1] / 2))

            # Draw the score
            text = self.font.render(f"Score: {self.score}", True, (200, 0, 0))
            self.screen.blit(text, (10, 10))

            pygame.display.update()

game = Game()
game.run()