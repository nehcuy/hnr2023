# imports
import pygame
import time
import random
import os
import sys

from . import game_over as g_o
from . import constants as c
sys.path.append("..")
import obstacle as obs

class Runner:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard

    # coordinates
    player_x = c.PLAYER_X_START
    player_y = c.PLAYER_Y_START
    player_lane = 0
    delta_x = 0
    delta_y = 0
    score = 0

    # player states
    player_frames = [pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_coloured", "Walk1-coloured.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_coloured", "Walk2-coloured.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_coloured", "Walk3-coloured.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_coloured", "Walk4-coloured.png"))]

    character_roll_frames = [pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_rolling", "Roll1.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_rolling", "Roll2.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_rolling", "Roll3.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_rolling", "Roll1.png")),]

    character_chopping_frames = [pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_chopping", "Attack_1.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_chopping", "Attack_2.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_chopping", "Attack_3.png")),
                        pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_chopping", "Attack_1.png")),]

    player = player_frames[0]
    player_frame_index = 0
    player_time_elapsed = 0

    def update_player(self, screen, delta_time, player_animation):
        self.player_time_elapsed += delta_time
        if self.player_time_elapsed >= c.PLAYER_ANIMATION_THRESHOLD:
            self.player_time_elapsed -= c.PLAYER_ANIMATION_THRESHOLD
            self.player_frame_index += 1
        if self.player_frame_index >= len(self.player_frames):
            self.player_frame_index = 0
        
        self.player = player_animation[self.player_frame_index]
        self.player = pygame.transform.smoothscale(self.player, 
            (c.PLAYER_ASPECT_RATIO * c.PLAYER_SCALE, c.PLAYER_SCALE))
        screen.blit(self.player, (self.player_x, self.player_y - c.PLAYER_Y_OFFSET))

    # obstacles
    obstacle_list = []
    obstacle_time_elapsed = 0
    obstacle_type_total_weight = c.OBSTACLE_TREE_CHANCE + c.OBSTACLE_SPIKE_CHANCE + c.OBSTACLE_ROCK_CHANCE

    def generate_new_obstacle(self, screen, lane):
        type_num = random.randint(1, self.obstacle_type_total_weight)
        if type_num <= c.OBSTACLE_TREE_CHANCE: # tree
            new_obstacle = obs.Obstacle(
                pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Tree.png")),
                "tree",
                lane,
                c.SCREEN_WIDTH)
        elif type_num <= c.OBSTACLE_TREE_CHANCE + c.OBSTACLE_ROCK_CHANCE: # rock
            new_obstacle = obs.Obstacle(
                pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Rock.png")),
                "rock",
                lane,
                c.SCREEN_WIDTH)
        else: # spike
            new_obstacle = obs.Obstacle(
                pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Spike.png")),
                "spike",
                lane,
                c.SCREEN_WIDTH)
        
        new_obstacle.surface = pygame.transform.smoothscale(new_obstacle.surface, 
            (c.OBSTACLE_ASPECT_RATIO * c.OBSTACLE_SCALE, c.OBSTACLE_SCALE))
        return new_obstacle
    def generate_with_lane_pattern(self, screen):
        lane_pattern = random.randint(0, len(c.OBSTACLE_LANE_PATTERNS) - 1)
        if c.OBSTACLE_LANE_PATTERNS[lane_pattern][0] == 1:
            self.obstacle_list.append(self.generate_new_obstacle(screen, 0))
        if c.OBSTACLE_LANE_PATTERNS[lane_pattern][1] == 1:
            self.obstacle_list.append(self.generate_new_obstacle(screen, 1))
        if c.OBSTACLE_LANE_PATTERNS[lane_pattern][2] == 1:
            self.obstacle_list.append(self.generate_new_obstacle(screen, 2))
        if c.OBSTACLE_LANE_PATTERNS[lane_pattern][3] == 1:
            self.obstacle_list.append(self.generate_new_obstacle(screen, 3))

    def update_obstacle(self, screen, x_speed, delta_time):
        self.obstacle_time_elapsed += delta_time
        if self.obstacle_time_elapsed >= c.OBSTACLE_CHANCE_THRESHOLD:
            self.obstacle_time_elapsed -= c.OBSTACLE_CHANCE_THRESHOLD
            # generate obstacle if within upper and lower bounds
            if len(self.obstacle_list) < c.OBSTACLE_LOWER_BOUND:
                self.generate_with_lane_pattern(screen)
            elif random.random() <= c.OBSTACLE_CHANCE:
                if len(self.obstacle_list) < c.OBSTACLE_UPPER_BOUND:
                    self.generate_with_lane_pattern(screen)

        
        for obstacle in self.obstacle_list[:]:
            obstacle.x_pos -= x_speed + (self.score // 2) # speed up obstacles
            if obstacle.x_pos < 0: # check out-of-bounds
                self.obstacle_list.remove(obstacle)
                continue
            # within bounds, draw on screen
            screen.blit(obstacle.surface, 
                    (obstacle.x_pos, c.LANE_Y_POSITIONS[obstacle.lane] - c.OBSTACLE_Y_OFFSET))
    
    def run(self):
        # initialize pygame
        pygame.init()
        screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll")

        is_running = True
        start_time = time.time()

        while is_running: # Game loop
            # update display
            pygame.display.update()

            # set fps
            clock = pygame.time.Clock()
            delta_time = clock.tick(c.FPS)

            # score
            score = int(time.time() - start_time)

            # draw
            screen.fill(c.GREY)
            floor_divider_1 = pygame.draw.rect(screen, c.WHITE, pygame.Rect(0, c.SCREEN_HEIGHT / 4, c.SCREEN_WIDTH, 5))
            floor_divider_2 = pygame.draw.rect(screen, c.WHITE, pygame.Rect(0, c.SCREEN_HEIGHT / 2, c.SCREEN_WIDTH, 5))
            floor_divider_3 = pygame.draw.rect(screen, c.WHITE, pygame.Rect(0, c.SCREEN_HEIGHT / 4 * 3, c.SCREEN_WIDTH, 5))
            
            # player animations
            if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]: # character rolls
                self.update_player(screen, delta_time, self.character_roll_frames)
            elif pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]: # character chops
                self.update_player(screen, delta_time, self.character_chopping_frames)
            else: # default idle animation
                self.update_player(screen, delta_time, self.player_frames)

            # draw & update obstacles
            self.update_obstacle(screen, delta_time, c.OBSTACLE_SPEED)

            # detect collision
            for obstacle in self.obstacle_list:
                if obstacle.lane == self.player_lane:
                    # check if player is within obstacle's x range
                    is_collision = obstacle.x_pos < self.player_x + c.PLAYER_ASPECT_RATIO * c.PLAYER_SCALE and obstacle.x_pos + 10 > self.player_x
                    
                    # check if player is chopping obstacle
                    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
                        if is_collision and obstacle.type == 'tree':
                            self.obstacle_list.remove(obstacle)
                            break

                    # check if player is rolling over obstacle
                    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
                        if is_collision and obstacle.type == 'rock':
                            self.obstacle_list.remove(obstacle)
                            break

                    if is_collision:
                        self.obstacle_list.clear()
                        is_running = False
                        g_o.GameOver(self.leaderboard, score).run()
                        break

            # draw score in top right corner
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(str(score), False, c.WHITE)
            screen.blit(text, (c.SCREEN_WIDTH - 50, 0))

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.player_lane > 0:
                            self.player_lane -= 1
                        self.player_y = c.LANE_Y_POSITIONS[self.player_lane]

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.player_lane < 3:
                            self.player_lane += 1
                        self.player_y = c.LANE_Y_POSITIONS[self.player_lane]
                        
            # player out-of-bounds constraints
            if self.player_y < 0:
                self.player_y = c.LANE_Y_POSITIONS[0]

            if self.player_y > c.SCREEN_HEIGHT:
                self.player_y = c.LANE_Y_POSITIONS[3]

            if self.player_x < 0:
                # TODO game over
                self.player_x = 0
            
            if self.player_x + c.PLAYER_SCALE > c.SCREEN_WIDTH:
                self.player_x = c.SCREEN_WIDTH - c.PLAYER_SCALE
                
            pygame.display.flip()

