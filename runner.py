# imports
import pygame
import time

# initialize pygame
pygame.init()

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
fps = 60
start = time.time()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# variables
player_x = 50
player_y = 450
delta_x = 0
delta_y = 0
gravity = 1
score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beaver Game")

is_running = True
while is_running:
	# score
	score = int(time.time() - start)

	# draw
	screen.fill(BLACK)
	player = pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
	floor = pygame.draw.rect(screen, WHITE, (0, 500, SCREEN_WIDTH, 5))

	# draw score in top right corner
	font = pygame.font.SysFont('Comic Sans MS', 30)
	text = font.render(str(score), False, WHITE)
	screen.blit(text, (SCREEN_WIDTH - 50, 0))

	# update display
	pygame.display.update()

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_x -= 50
			if event.key == pygame.K_RIGHT:
				player_x += 50
			if event.key == pygame.K_UP:
				player_y -= 50
			if event.key == pygame.K_DOWN:
				player_y += 50
			if event.key == pygame.K_SPACE and delta_y == 0:
				delta_y = 18

	if delta_y > 0 or player_y < 450: # if player above ground
		player_y -= delta_y
		delta_y -= gravity

	if player_y > 450: # in case player falls through ground
		player_y = 450

	if player_y == 450 and delta_y < 0: # if player on ground, reset delta_y
		delta_y = 0

	pygame.display.flip()
pygame.quit()

	
