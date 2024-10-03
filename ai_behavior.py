import random
from settings import *

class State:
    """Base state class for enemy AI."""
    def execute(self, enemy, player):
        pass

class PatrolState(State):
    """State for patrolling along points."""
    def execute(self, enemy, player):
        if enemy.detect_player(player):
            enemy.state = ChaseState()  # Switch to chase state
        else:
            enemy.move()  # Continue patrolling

class ChaseState(State):
    """State for chasing the player."""
    def execute(self, enemy, player):
        if not enemy.detect_player(player):
            enemy.state = PatrolState()  # Lose player, return to patrol
        else:
            self.chase_player(enemy, player)

    def chase_player(self, enemy, player):
        """Move enemy towards player."""
        dx, dy = player.rect.x - enemy.rect.x, player.rect.y - enemy.rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            dx, dy = dx / dist, dy / dist
        enemy.rect.x += dx * enemy.speed
        enemy.rect.y += dy * enemy.speed

class RandomBehaviorTree:
    """Simple random behavior tree for AI."""
    def __init__(self, enemy):
        self.enemy = enemy
        self.behaviors = [PatrolState(), ChaseState()]
        self.current_behavior = random.choice(self.behaviors)

    def execute(self, player):
        self.current_behavior.execute(self.enemy, player)

if __name__ == "__main__":
    # Testing simple AI states
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    patrol_points = [(100, 100), (400, 100), (400, 400), (100, 400)]
    enemy = Enemy(100, 100, patrol_points)
    player = Player(200, 200)
    ai = RandomBehaviorTree(enemy)
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Run AI behavior
        ai.execute(player)

        # Render player and enemy
        player.render(screen)
        enemy.render(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
