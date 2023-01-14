# imports
import pygame
import time
import random
import os
import sys

from . import game_over as g_o
from . import leaderboard as lb
from . import constants as c
sys.path.append("..")
import obstacle as obs

class Runner:
    # coordinates
    player_x = c.PLAYER_X_START
    player_y = c.PLAYER_Y_START
    player_lane = 0
    delta_x = 0
    delta_y = 0
    score = 0

    # player
    player_frames = [pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_uncoloured", "Walk-4.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_uncoloured", "Walk-3.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_uncoloured", "Walk-2.png")),
						pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_uncoloured", "Walk-1.png"))]
    player = player_frames[0]
    player_frame_index = 0
    player_time_elapsed = 0

    def update_player(self, screen, delta_time):
        self.player_time_elapsed += delta_time
        if self.player_time_elapsed >= c.PLAYER_ANIMATION_THRESHOLD:
            self.player_time_elapsed -= c.PLAYER_ANIMATION_THRESHOLD
            self.player_frame_index += 1
        if self.player_frame_index >= len(self.player_frames):
            self.player_frame_index = 0
        
        self.player = self.player_frames[self.player_frame_index]
        self.player = pygame.transform.smoothscale(self.player, 
            (c.PLAYER_ASPECT_RATIO * c.PLAYER_SCALE, c.PLAYER_SCALE))
        screen.blit(self.player, (self.player_x, self.player_y - c.PLAYER_Y_OFFSET))

    # obstacles
    obstacle_list = []
    obstacle_time_elapsed = 0

    def update_obstacle(self, screen, x_speed, delta_time):
        self.obstacle_time_elapsed += delta_time
        if self.obstacle_time_elapsed >= c.OBSTACLE_CHANCE_THRESHOLD:
            self.obstacle_time_elapsed -= c.OBSTACLE_CHANCE_THRESHOLD
            if random.random() <= c.OBSTACLE_CHANCE:
                new_obstacle = obs.Obstacle(
                    pygame.image.load(os.path.join(c.APP_FOLDER, "images", "character_uncoloured", "Walk-4.png")),
                    "tree",
                    random.randint(0, 3),
                    c.SCREEN_WIDTH)
                new_obstacle.surface = pygame.transform.smoothscale(new_obstacle.surface, (10, 10))
                self.obstacle_list.append(new_obstacle)
        
        for obstacle in self.obstacle_list[:]:
            obstacle.x_pos -= x_speed
            if obstacle.x_pos < 0: # check out-of-bounds
                self.obstacle_list.remove(obstacle)
                continue
            # within bounds, draw on screen
            screen.blit(obstacle.surface, 
                    (obstacle.x_pos, c.LANE_Y_POSITIONS[obstacle.lane]))
    

    def run(self):
        # initialize pygame
        pygame.init()
        screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll")

        is_running = True
        start_time = time.time()
        
        while is_running:
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
            
            # player animation
            self.update_player(screen, delta_time)

            # draw & update obstacles
            self.update_obstacle(screen, delta_time, c.OBSTACLE_SPEED)

            # detect collision
            for obstacle in self.obstacle_list:
                if obstacle.lane == self.player_lane:
                    if obstacle.x_pos < self.player_x + c.PLAYER_ASPECT_RATIO * c.PLAYER_SCALE and obstacle.x_pos + 10 > self.player_x:
                        self.obstacle_list.clear()
                        is_running = False
                        g_o.GameOver(score).run()

            # draw score in top right corner
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(str(score), False, c.WHITE)
            screen.blit(text, (c.SCREEN_WIDTH - 50, 0))

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_x -= c.PLAYER_X_SPEED * delta_time
                    if event.key == pygame.K_RIGHT:
                        self.player_x += c.PLAYER_X_SPEED * delta_time
                    if event.key == pygame.K_UP:
                        if self.player_lane > 0:
                            self.player_lane -= 1
                        self.player_y = c.LANE_Y_POSITIONS[self.player_lane]
                    if event.key == pygame.K_DOWN:
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

