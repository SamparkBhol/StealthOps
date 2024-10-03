import pygame

class InputHandler:
    """Handles keyboard and mouse inputs for the game."""
    def __init__(self):
        self.keys = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d,
            'action': pygame.K_SPACE
        }
        self.mouse_pos = (0, 0)
        self.mouse_pressed = False

    def process_keyboard_input(self, player):
        """Processes keyboard input for player movement."""
        keys = pygame.key.get_pressed()

        if keys[self.keys['up']]:
            player.move(0, -1)
        if keys[self.keys['down']]:
            player.move(0, 1)
        if keys[self.keys['left']]:
            player.move(-1, 0)
        if keys[self.keys['right']]:
            player.move(1, 0)

        if keys[self.keys['action']]:
            print("Action button pressed")

    def process_mouse_input(self):
        """Processes mouse position and button state."""
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pressed = pygame.mouse.get_pressed()[0]

    def handle_input(self, player):
        """Handles both keyboard and mouse input."""
        self.process_keyboard_input(player)
        self.process_mouse_input()

        if self.mouse_pressed:
            print(f"Mouse clicked at {self.mouse_pos}")

class Player:
    """Represents the player controlled by keyboard and mouse input."""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5

    def move(self, dx, dy):
        """Moves the player by the given offset."""
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        """Draws the player on the screen."""
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

def main():
    """Main game loop with input handling."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Create player and input handler
    player = Player(400, 300, 50, 50)
    input_handler = InputHandler()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle input
        input_handler.handle_input(player)

        # Draw everything
        screen.fill((0, 0, 0))
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
