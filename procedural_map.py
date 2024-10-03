import pygame
import random
from settings import *

class ProceduralMap:
    def __init__(self, player, camera):
        self.player = player
        self.camera = camera
        self.tiles = []
        self.generate_map()

    def generate_map(self):
        """Generate a procedural map using random tiles."""
        self.tiles = []
        for x in range(0, MAP_WIDTH, TILE_SIZE):
            for y in range(0, MAP_HEIGHT, TILE_SIZE):
                if random.random() < 0.2:
                    self.tiles.append(Tile(x, y, 'wall'))
                else:
                    self.tiles.append(Tile(x, y, 'floor'))

    def update(self):
        """Update any changes to the map."""
        pass  # Map is static for now, could add moving parts or dynamic elements.

    def render(self, screen):
        """Render the procedural map."""
        for tile in self.tiles:
            tile.render(screen, self.camera)

class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.tile_type = tile_type
        if self.tile_type == 'wall':
            self.color = WALL_COLOR
        else:
            self.color = FLOOR_COLOR

    def render(self, screen, camera):
        """Render individual tiles based on their type."""
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        pygame.draw.rect(screen, self.color, pygame.Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE))

class Camera:
    def __init__(self, player):
        self.player = player
        self.x = 0
        self.y = 0
        self.update()

    def update(self):
        """Update the camera position based on the player's position."""
        self.x = self.player.x - CAMERA_WIDTH // 2
        self.y = self.player.y - CAMERA_HEIGHT // 2

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player()
    camera = Camera(player)
    procedural_map = ProceduralMap(player, camera)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        procedural_map.render(screen)
        pygame.display.flip()

    pygame.quit()