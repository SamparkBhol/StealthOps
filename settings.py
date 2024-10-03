# Game Settings and Configurations
import pygame  
import os
# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

# Player Settings
PLAYER_SPEED = 5
PLAYER_COLOR = (0, 255, 0)
PLAYER_SIZE = 20

# Enemy Settings
NUM_ENEMIES = 5
ENEMY_SPEED = 2
ENEMY_COLOR = (255, 0, 0)
ENEMY_VISION_ANGLE = 90
ENEMY_VISION_DISTANCE = 200

# Camera Settings
CAMERA_WIDTH = SCREEN_WIDTH // 2
CAMERA_HEIGHT = SCREEN_HEIGHT // 2

# Procedural Map Settings
MAP_WIDTH = 2000
MAP_HEIGHT = 2000
TILE_SIZE = 50
WALL_COLOR = (100, 100, 100)
FLOOR_COLOR = (200, 200, 200)

# Game States
GAME_STATE_PLAYING = "playing"
GAME_STATE_PAUSED = "paused"

# Movement keys
MOVEMENT_KEYS = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0)
}

# AI Behavior Settings
AI_PATROL_SPEED = 1
AI_DETECTION_RADIUS = 100
AI_LOS_COLOR = (255, 255, 0)

# Debugging options
DEBUG_MODE = False
SHOW_VISION_CONES = True

# Pathfinding Parameters
PATHFINDING_GRID_SIZE = 50
A_STAR_MAX_SEARCH_RADIUS = 500

# Other game parameters
MAX_LEVELS = 10
LEVEL_COMPLETE_MESSAGE = "Level Complete!"


# Configuration for game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 70

# Player movement controls
CONTROLS = {
    pygame.K_w: (0, -1),   # Move up
    pygame.K_s: (0, 1),    # Move down
    pygame.K_a: (-1, 0),   # Move left
    pygame.K_d: (1, 0),    # Move right
}

# AI parameters
ENEMY_VISION_RADIUS = 100
ENEMY_PATROL_SPEED = 2

# Game assets directory
ASSETS_DIR = os.path.join(os.getcwd(), 'assets')