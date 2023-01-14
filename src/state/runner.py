# imports
import pygame
import time
import random
from . import constants

class Runner:
    # variables
    player_x = constants.PLAYER_X_START
    player_y = constants.PLAYER_Y_START
    player_lane = 0
    delta_x = 0
    delta_y = 0
    gravity = 1
    score = 0
    spawn_index = random.randrange(0, len(constants.LANE_Y_POSITIONS) - 1)
    active = True

    def run(self):
        # initialize pygame
        pygame.init()
        screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll")

        is_running = True
        
        while is_running:
            # score
            score = int(time.time() - constants.START_TIME)

            # draw
            screen.fill(constants.BLACK)
            player = pygame.draw.rect(screen, constants.BLUE, pygame.Rect(self.player_x, self.player_y - 25, 50, 50))
            floor_divider_1 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 4, constants.SCREEN_WIDTH, 5))
            floor_divider_2 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, 5))
            floor_divider_3 = pygame.draw.rect(screen, constants.WHITE, pygame.Rect(0, constants.SCREEN_HEIGHT / 4 * 3, constants.SCREEN_WIDTH, 5))
            obstacle0 = pygame.draw.rect(screen, constants.RED, pygame.Rect(constants.OBSTACLE_START_X_POSITIONS[0], constants.LANE_Y_POSITIONS[self.spawn_index], 20, 20))

            # draw score in top right corner
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(str(score), False, constants.WHITE)
            screen.blit(text, (constants.SCREEN_WIDTH - 50, 0))

            # update display
            pygame.display.update()

            # set fps
            clock = pygame.time.Clock()
            delta_time = clock.tick(constants.FPS)

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
                        player_y = constants.LANE_Y_POSITIONS[self.player_lane]
                    if event.key == pygame.K_DOWN:
                        if self.player_lane < 3:
                            self.player_lane += 1
                        player_y = constants.LANE_Y_POSITIONS[self.player_lane]

            for i in range(len(constants.OBSTACLE_START_X_POSITIONS)):
                if self.active:
                    constants.OBSTACLE_START_X_POSITIONS[i] -= constants.OBSTACLE_X_SPEED
                    if constants.OBSTACLE_START_X_POSITIONS[i] < -50:
                        spawn_index = random.randint(0, len(constants.LANE_Y_POSITIONS) - 1)
                        constants.OBSTACLE_START_X_POSITIONS[i] = random.randint(900, 1000)
                        
            # out-of-bounds constraints
            if self.player_y < 0:
                player_y = constants.LANE_Y_POSITIONS[0]

            if self.player_y > constants.SCREEN_HEIGHT:
                player_y = constants.LANE_Y_POSITIONS[3]

            if self.player_x < 0:
                # TODO game over
                player_x = 0
            
            if self.player_x > constants.SCREEN_WIDTH:
                player_x = constants.SCREEN_WIDTH - (constants.PLAYER_X_SPEED * delta_time)
                
            pygame.display.flip()
        pygame.quit()

	
