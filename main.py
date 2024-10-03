import pygame
from settings import *
from player import Player
from procedural_map import ProceduralMap
from enemy import Enemy
from camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("3D Stealth Espionage Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.camera = Camera(self.player)
        self.map = ProceduralMap(self.player, self.camera)
        self.enemies = []
        self.spawn_enemies()

    def spawn_enemies(self):
        """Generate enemies on the map."""
        for i in range(NUM_ENEMIES):
            enemy = Enemy(self.map)
            self.enemies.append(enemy)

    def run(self):
        """Main game loop."""
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()

    def handle_events(self):
        """Handle player inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update game state."""
        self.player.update()
        for enemy in self.enemies:
            enemy.update(self.player)
        self.map.update()
        self.camera.update()

    def render(self):
        """Render everything on the screen."""
        self.screen.fill(BACKGROUND_COLOR)
        self.map.render(self.screen)
        self.player.render(self.screen)
        for enemy in self.enemies:
            enemy.render(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
