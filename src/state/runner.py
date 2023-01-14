# imports
import pygame
import time
import random

# initialize pygame
pygame.init()



def run():
	# constants
	SCREEN_WIDTH = 800
	SCREEN_HEIGHT = 600
	PLAYER_X_SPEED = SCREEN_WIDTH/100
	PLAYER_X_START = 0
	PLAYER_Y_START = SCREEN_HEIGHT/8
	OBSTACLE_X_SPEED = 5
	OBSTACLE_START_X_POSITIONS = [900, 1000, 850]
	LANE_Y_POSITIONS = [PLAYER_Y_START, 
		PLAYER_Y_START + SCREEN_HEIGHT / 4, 
		PLAYER_Y_START + SCREEN_HEIGHT / 2,
		PLAYER_Y_START + SCREEN_HEIGHT / 4 * 3]
	FPS = 60
	START_TIME = time.time()

	# colors
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	# variables
	player_x = PLAYER_X_START
	player_y = PLAYER_Y_START
	player_lane = 0
	delta_x = 0
	delta_y = 0
	gravity = 1
	score = 0
	spawn_index = random.randrange(0, len(LANE_Y_POSITIONS) - 1)
	active = True

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Hack and Roll")

	is_running = True
	
	while is_running:
		# score
		score = int(time.time() - START_TIME)

		# draw
		screen.fill(BLACK)
		player = pygame.draw.rect(screen, BLUE, pygame.Rect(player_x, player_y - 25, 50, 50))
		floor_divider_1 = pygame.draw.rect(screen, WHITE, pygame.Rect(0, SCREEN_HEIGHT / 4, SCREEN_WIDTH, 5))
		floor_divider_2 = pygame.draw.rect(screen, WHITE, pygame.Rect(0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, 5))
		floor_divider_3 = pygame.draw.rect(screen, WHITE, pygame.Rect(0, SCREEN_HEIGHT / 4 * 3, SCREEN_WIDTH, 5))
		obstacle0 = pygame.draw.rect(screen, RED, pygame.Rect(OBSTACLE_START_X_POSITIONS[0], LANE_Y_POSITIONS[spawn_index], 20, 20))

		# draw score in top right corner
		font = pygame.font.SysFont('Arial', 30)
		text = font.render(str(score), False, WHITE)
		screen.blit(text, (SCREEN_WIDTH - 50, 0))

		# update display
		pygame.display.update()

		# set fps
		clock = pygame.time.Clock()
		delta_time = clock.tick(FPS)

		# event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player_x -= PLAYER_X_SPEED * delta_time
				if event.key == pygame.K_RIGHT:
					player_x += PLAYER_X_SPEED * delta_time
				if event.key == pygame.K_UP:
					if player_lane > 0:
						player_lane -= 1
					player_y = LANE_Y_POSITIONS[player_lane]
				if event.key == pygame.K_DOWN:
					if player_lane < 3:
						player_lane += 1
					player_y = LANE_Y_POSITIONS[player_lane]

		for i in range(len(OBSTACLE_START_X_POSITIONS)):
			if active:
				OBSTACLE_START_X_POSITIONS[i] -= (OBSTACLE_X_SPEED + (score // 2))
				if OBSTACLE_START_X_POSITIONS[i] < -50:
					spawn_index = random.randint(0, len(LANE_Y_POSITIONS) - 1)
					OBSTACLE_START_X_POSITIONS[i] = random.randint(900, 1000)
					
		# out-of-bounds constraints
		if player_y < 0:
			player_y = LANE_Y_POSITIONS[0]

		if player_y > SCREEN_HEIGHT:
			player_y = LANE_Y_POSITIONS[3]

		if player_x < 0:
			# TODO game over
			player_x = 0
		
		if player_x > SCREEN_WIDTH:
			player_x = SCREEN_WIDTH - (PLAYER_X_SPEED * delta_time)
			
		pygame.display.flip()
	pygame.quit()

	
