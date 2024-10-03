import pygame
from settings import *
import pygame
from settings import PLAYER_WIDTH, PLAYER_HEIGHT  # Import player dimensions

class Player:
    def __init__(self, x=100, y=100):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT) 

class Player:
    def __init__(self, x=100, y=100):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED
        self.crouching = False
        self.hidden = False

    def move(self, keys):
        """Handle player movement."""
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        # Apply crouch speed reduction
        if self.crouching:
            dx *= CROUCH_SPEED_REDUCTION
            dy *= CROUCH_SPEED_REDUCTION

        # Update player position
        self.rect.x += dx
        self.rect.y += dy

        # Keep player within screen boundaries
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def crouch(self, key_down):
        """Toggle crouching."""
        if key_down:
            self.crouching = not self.crouching

    def hide(self, key_down, hiding_spot_rect):
        """Hide player if within a hiding spot."""
        if key_down and self.rect.colliderect(hiding_spot_rect):
            self.hidden = True
        else:
            self.hidden = False

    def render(self, screen):
        """Render the player."""
        color = HIDDEN_COLOR if self.hidden else PLAYER_COLOR
        pygame.draw.rect(screen, color, self.rect)

# Simple Hiding Spot Example
class HidingSpot:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def render(self, screen):
        pygame.draw.rect(screen, HIDING_SPOT_COLOR, self.rect)


if __name__ == "__main__":
    # Initialize the game and create a player
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(200, 200)
    hiding_spot = HidingSpot(300, 300, 50, 50)
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        keys = pygame.key.get_pressed()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    player.crouch(True)
                if event.key == pygame.K_h:
                    player.hide(True, hiding_spot.rect)

        # Player movement
        player.move(keys)

        # Render hiding spot and player
        hiding_spot.render(screen)
        player.render(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()