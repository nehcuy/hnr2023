# imports
import pygame
import time
import random
import os

from . import constants
from . import Obstacle

class Runner:
    # coordinates
    player_x = constants.PLAYER_X_START
    player_y = constants.PLAYER_Y_START
    player_lane = 0
    delta_x = 0
    delta_y = 0
    score = 0

    # player images
    player_frames = [pygame.image.load(os.path.join(constants.APP_FOLDER, "images", "character_frames", "Walk-4.png")),
						pygame.image.load(os.path.join(constants.APP_FOLDER, "images", "character_frames", "Walk-3.png")),
						pygame.image.load(os.path.join(constants.APP_FOLDER, "images", "character_frames", "Walk-2.png")),
						pygame.image.load(os.path.join(constants.APP_FOLDER, "images", "character_frames", "Walk-1.png"))]
    player_frame_index = 0
    player_time_elapsed = 0

    def update_player(self, player_frames, delta_time):
        self.player_time_elapsed += delta_time
        if self.player_time_elapsed >= constants.PLAYER_ANIMATION_THRESHOLD:
            self.player_time_elapsed -= constants.PLAYER_ANIMATION_THRESHOLD
            self.player_frame_index += 1
        if self.player_frame_index >= len(player_frames):
            self.player_frame_index = 0
        return player_frames[self.player_frame_index]

    # obstacles
    obstacle_list = []
    obstacle_chance = 0.05
    obstacle_1 = Obstacle.Obstacle( 
        pygame.image.load(os.path.join(constants.APP_FOLDER, "images", "character_frames", "Walk-4.png")),
        "tree",
        2, 500)
    obstacle_1.surface = pygame.transform.smoothscale(obstacle_1.surface, (10, 10))
    obstacle_list.append(obstacle_1)

    def update_obstacle(self, screen, x_speed):
        for obstacle in self.obstacle_list[:]:
            obstacle.x_pos -= x_speed
            if obstacle.x_pos < 0: # check out-of-bounds
                self.obstacle_list.remove(obstacle)
                continue
            # within bounds, draw on screen
            screen.blit(obstacle.surface, 
                    (obstacle.x_pos, constants.LANE_Y_POSITIONS[obstacle.lane]))
    

    def run(self):
        # initialize pygame
        pygame.init()
        screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll")

        is_running = True
        
        while is_running:
            # update display
            pygame.display.update()

            # set fps
            clock = pygame.time.Clock()
            delta_time = clock.tick(constants.FPS)

            # score
            score = int(time.time() - constants.START_TIME)

            # draw
            screen.fill(constants.BLACK)
            floor_divider_1 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 4, constants.SCREEN_WIDTH, 5))
            floor_divider_2 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, 5))
            floor_divider_3 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 4 * 3, constants.SCREEN_WIDTH, 5))
            
            # player animation
            player = self.update_player(self.player_frames, delta_time)
            player = pygame.transform.smoothscale(player, (constants.PLAYER_ASPECT_RATIO * constants.PLAYER_SCALE, constants.PLAYER_SCALE))
            screen.blit(player, (self.player_x, self.player_y - constants.PLAYER_Y_OFFSET))

            # draw & update obstacles
            self.update_obstacle(screen, 10)
                

            # draw score in top right corner
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(str(score), False, constants.WHITE)
            screen.blit(text, (constants.SCREEN_WIDTH - 50, 0))

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_x -= constants.PLAYER_X_SPEED * delta_time
                    if event.key == pygame.K_RIGHT:
                        self.player_x += constants.PLAYER_X_SPEED * delta_time
                    if event.key == pygame.K_UP:
                        if self.player_lane > 0:
                            self.player_lane -= 1
                        self.player_y = constants.LANE_Y_POSITIONS[self.player_lane]
                    if event.key == pygame.K_DOWN:
                        if self.player_lane < 3:
                            self.player_lane += 1
                        self.player_y = constants.LANE_Y_POSITIONS[self.player_lane]
                        
            # player out-of-bounds constraints
            if self.player_y < 0:
                self.player_y = constants.LANE_Y_POSITIONS[0]

            if self.player_y > constants.SCREEN_HEIGHT:
                self.player_y = constants.LANE_Y_POSITIONS[3]

            if self.player_x < 0:
                # TODO game over
                self.player_x = 0
            
            if self.player_x + constants.PLAYER_SCALE > constants.SCREEN_WIDTH:
                self.player_x = constants.SCREEN_WIDTH - constants.PLAYER_SCALE
                
            pygame.display.flip()
        pygame.quit()
