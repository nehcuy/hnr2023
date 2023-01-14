import pygame
import button
import main

import state.constants as c

class Tutorial:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Tutorial")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = 45
        self.back_button = button.Button(button_width, button_height, button_x, button_y, "Back")

    def run(self):
        running = True
        while running:
            self.screen.fill(c.GREY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_pressed(pygame.mouse.get_pos()):
                        main.Main().run()

            self.back_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()