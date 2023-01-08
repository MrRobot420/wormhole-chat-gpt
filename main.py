import random
import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('My Game')

# Set the background color
bg_color = (255, 255, 255)

# Create the player object
player_color = (0, 0, 0)
player_pos = (200, 200)
player_radius = 20

# Create a list to store the enemy objects
enemies = []

# Create the enemy objects
enemy_color = (0, 100, 0)
enemy_size = (20, 20)

# Create a font object
font = pygame.font.Font(None, 36)

# Initialize the score
score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the score
    score_increased = False

    # Add new enemies to the list
    if len(enemies) < 20:
        enemies.append((random.randint(0, window_size[0]), random.randint(0, window_size[1])))

    # Get the keys that are being pressed
    keys = pygame.key.get_pressed()

    # Update the player's position based on the keys that are being pressed
    if keys[pygame.K_w]:
        player_pos = (player_pos[0], player_pos[1] - 1)
    if keys[pygame.K_s]:
        player_pos = (player_pos[0], player_pos[1] + 1)
    if keys[pygame.K_a]:
        player_pos = (player_pos[0] - 1, player_pos[1])
    if keys[pygame.K_d]:
        player_pos = (player_pos[0] + 1, player_pos[1])

    # Draw the background
    screen.fill(bg_color)

    # Draw the player
    pygame.draw.circle(screen, player_color, player_pos, player_radius)

    # Draw the enemies
    for enemy_pos in enemies:
        pygame.draw.rect(screen, enemy_color, (enemy_pos, enemy_size))

        # Check if the player is colliding with the enemy
        if pygame.Rect(enemy_pos, enemy_size).colliderect(player_pos, (player_radius*2, player_radius*2)):
            # Swallow the enemy
            enemies.remove(enemy_pos)

            # Increase the player's size
            player_radius += 5
            score += 100
            score_increased = True

    # Update the score
    if score_increased:
        score += 1

    # Draw the score
    text = font.render(f"Score: {score}", True, (200, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
