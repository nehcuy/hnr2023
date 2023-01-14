import time
import os
import sys

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_X_SPEED = SCREEN_WIDTH / 100
PLAYER_X_START = 0
PLAYER_Y_START = SCREEN_HEIGHT / 8
PLAYER_Y_OFFSET = SCREEN_HEIGHT / 10
PLAYER_ASPECT_RATIO = 585/431
PLAYER_SCALE = SCREEN_HEIGHT / 5 # width of player
PLAYER_ANIMATION_THRESHOLD = 100 # milliseconds till new frame
OBSTACLE_SPEED = SCREEN_WIDTH / 200
OBSTACLE_CHANCE = 0.5 # % chance to spawn an obstacle
OBSTACLE_CHANCE_THRESHOLD = 50 # milliseconds till chance check
LANE_Y_POSITIONS = [PLAYER_Y_START, 
    PLAYER_Y_START + SCREEN_HEIGHT / 4, 
    PLAYER_Y_START + SCREEN_HEIGHT / 2,
    PLAYER_Y_START + SCREEN_HEIGHT / 4 * 3]
FPS = 60
START_TIME = time.time()
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)