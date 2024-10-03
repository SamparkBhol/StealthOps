import pygame

class Wall:
    """Represents a wall object in the game."""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def render(self, screen, color=(255, 0, 0)):
        """Render the wall."""
        pygame.draw.rect(screen, color, self.rect)

class Door:
    """Represents a door that the player can interact with."""
    def __init__(self, x, y, width, height, locked=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.locked = locked

    def toggle(self):
        """Toggle door's locked state."""
        self.locked = not self.locked

    def render(self, screen, color=(0, 255, 0)):
        """Render the door."""
        color = (0, 0, 255) if self.locked else color
        pygame.draw.rect(screen, color, self.rect)

class Obstacle:
    """Represents an obstacle in the game."""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def render(self, screen, color=(255, 255, 0)):
        """Render the obstacle."""
        pygame.draw.rect(screen, color, self.rect)


if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    # Create some walls, doors, and obstacles
    walls = [Wall(50, 50, 100, 10), Wall(150, 50, 10, 100)]
    doors = [Door(200, 50, 50, 10), Door(200, 200, 10, 50)]
    obstacles = [Obstacle(300, 300, 50, 50)]

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Render all objects
        for wall in walls:
            wall.render(screen)

        for door in doors:
            door.render(screen)

        for obstacle in obstacles:
            obstacle.render(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
