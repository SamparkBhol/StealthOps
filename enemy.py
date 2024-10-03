import pygame
from settings import *
from pathfinding import a_star_pathfinding

class Enemy:
    def __init__(self, x, y, patrol_points):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.patrol_points = patrol_points
        self.current_point = 0
        self.speed = ENEMY_SPEED
        self.vision_cone = VisionCone(self.rect.center, VISION_CONE_RADIUS, VISION_CONE_ANGLE)
        self.patrol_direction = 1

    def move(self):
        """Move enemy along patrol points."""
        target_x, target_y = self.patrol_points[self.current_point]
        dx, dy = target_x - self.rect.x, target_y - self.rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist > 0:
            dx, dy = dx / dist, dy / dist
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Check if reached current patrol point
        if dist < PATROL_REACH_TOLERANCE:
            self.current_point = (self.current_point + self.patrol_direction) % len(self.patrol_points)

    def reverse_patrol(self):
        """Reverse patrol direction."""
        self.patrol_direction *= -1

    def detect_player(self, player):
        """Check if player is within vision cone."""
        return self.vision_cone.is_player_detected(player)

    def render(self, screen):
        """Render enemy and vision cone."""
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)
        self.vision_cone.update(self.rect.center)
        self.vision_cone.render(screen)

# Vision Cone Class for Detection
class VisionCone:
    def __init__(self, origin, radius, angle):
        self.origin = origin
        self.radius = radius
        self.angle = angle

    def is_player_detected(self, player):
        """Simple detection logic to check if player is within the cone."""
        player_vec = pygame.Vector2(player.rect.center) - pygame.Vector2(self.origin)
        distance = player_vec.length()
        if distance > self.radius:
            return False
        angle_between = player_vec.angle_to(pygame.Vector2(1, 0))
        if abs(angle_between) < self.angle / 2:
            return True
        return False

    def update(self, new_origin):
        """Update the vision cone's origin (follows enemy)."""
        self.origin = new_origin

    def render(self, screen):
        """Render vision cone (debugging purposes)."""
        pygame.draw.circle(screen, VISION_CONE_COLOR, self.origin, self.radius, 1)


if __name__ == "__main__":
    # Initialize game window and create an enemy
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    patrol_points = [(100, 100), (400, 100), (400, 400), (100, 400)]
    enemy = Enemy(100, 100, patrol_points)
    player = Player(200, 200)
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move and render enemy
        enemy.move()
        enemy.render(screen)

        # Detect player
        if enemy.detect_player(player):
            print("Player detected!")

        # Render player
        player.render(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
