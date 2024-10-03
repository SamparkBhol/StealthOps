import pygame

class Collider:
    """Basic collider class for handling collision detection between objects."""
    def __init__(self, rect):
        self.rect = rect

    def check_collision(self, other):
        """Checks for collision with another Collider object."""
        return self.rect.colliderect(other.rect)

class PlayerCollider(Collider):
    """Handles player-specific collisions."""
    def __init__(self, rect):
        super().__init__(rect)

    def handle_collision(self, collidables):
        """Handles player-specific collision behavior."""
        for obj in collidables:
            if self.check_collision(obj):
                if isinstance(obj, EnemyCollider):
                    print("Collision with enemy!")
                elif isinstance(obj, ObjectCollider):
                    print("Collision with object!")

class EnemyCollider(Collider):
    """Handles enemy-specific collisions."""
    def __init__(self, rect):
        super().__init__(rect)

    def patrol(self, direction, speed, bounds):
        """Simulate enemy patrol movement and detect boundary collisions."""
        if direction == 'horizontal':
            self.rect.x += speed
            if self.rect.left < bounds[0] or self.rect.right > bounds[1]:
                speed *= -1
        elif direction == 'vertical':
            self.rect.y += speed
            if self.rect.top < bounds[0] or self.rect.bottom > bounds[1]:
                speed *= -1

class ObjectCollider(Collider):
    """Handles static object collisions (e.g., walls, obstacles)."""
    def __init__(self, rect):
        super().__init__(rect)

class CollisionManager:
    """Manages all collision detection and resolution."""
    def __init__(self):
        self.player = None
        self.enemies = []
        self.objects = []

    def add_player(self, player):
        """Adds player to collision manager."""
        self.player = player

    def add_enemy(self, enemy):
        """Adds enemy to collision manager."""
        self.enemies.append(enemy)

    def add_object(self, obj):
        """Adds static object to collision manager."""
        self.objects.append(obj)

    def update(self):
        """Checks for collisions between the player, enemies, and objects."""
        if self.player:
            self.player.handle_collision(self.enemies + self.objects)
        for enemy in self.enemies:
            for obj in self.objects:
                if enemy.check_collision(obj):
                    print("Enemy collided with object")

def main():
    """Basic setup for testing collisions."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Creating a player and some objects for collision
    player = PlayerCollider(pygame.Rect(100, 100, 50, 50))
    enemy = EnemyCollider(pygame.Rect(300, 300, 50, 50))
    wall = ObjectCollider(pygame.Rect(400, 400, 100, 20))

    collision_manager = CollisionManager()
    collision_manager.add_player(player)
    collision_manager.add_enemy(enemy)
    collision_manager.add_object(wall)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Simulate enemy patrol
        enemy.patrol('horizontal', 2, (0, 800))

        # Update collision system
        collision_manager.update()

        screen.fill((0, 0, 0))

        # Drawing rectangles to visualize
        pygame.draw.rect(screen, (0, 255, 0), player.rect)
        pygame.draw.rect(screen, (255, 0, 0), enemy.rect)
        pygame.draw.rect(screen, (255, 255, 0), wall.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
