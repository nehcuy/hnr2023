import os
import sys

# constants

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# player
PLAYER_X_SPEED = SCREEN_WIDTH / 100
PLAYER_X_START = 0
PLAYER_Y_START = SCREEN_HEIGHT / 8
PLAYER_Y_OFFSET = SCREEN_HEIGHT / 10
PLAYER_ASPECT_RATIO = 569/450
PLAYER_SCALE = SCREEN_HEIGHT / 5 # width of player
PLAYER_ANIMATION_THRESHOLD = 100 # milliseconds till new frame

# obstacle
OBSTACLE_Y_OFFSET = SCREEN_HEIGHT / 20
OBSTACLE_ASPECT_RATIO = 569/450
OBSTACLE_SCALE = SCREEN_HEIGHT / 8 # width of obstacle
OBSTACLE_SPEED = SCREEN_WIDTH / 200
OBSTACLE_CHANCE = 0.4 # % chance to spawn an obstacle
OBSTACLE_CHANCE_THRESHOLD = 40 # milliseconds till chance check
    # obstacle type chance -> weight is relative between tree & rock & spike
OBSTACLE_TREE_CHANCE = 10 # weight of tree spawn
OBSTACLE_ROCK_CHANCE = 10 # weight of rock spawn
OBSTACLE_SPIKE_CHANCE = 10 # weight of spike spawn
OBSTACLE_LANE_PATTERNS = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
] # 1 to spawn, first index = spawn in top lane
OBSTACLE_LOWER_BOUND = 3 # if less obstacles, guarantee obstacle generation
OBSTACLE_UPPER_BOUND = 8 # if more obstacles, no generation

# background
BACKGROUND_ANIMATION_THRESHOLD = 100 # milliseconds till new frame

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# others
LANE_Y_POSITIONS = [PLAYER_Y_START, 
    PLAYER_Y_START + SCREEN_HEIGHT / 4, 
    PLAYER_Y_START + SCREEN_HEIGHT / 2,
    PLAYER_Y_START + SCREEN_HEIGHT / 4 * 3]
FPS = 60
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
LEADERBOARD_FILE = os.path.join(APP_FOLDER, 'state', 'leaderboard.txt')
TUTORIAL_TEXT_SPACING = 40
