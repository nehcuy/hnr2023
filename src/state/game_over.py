import pygame
import button

from . import leaderboard
from . import runner

class GameOver:
    def __init__(self, score):
        self.score = score
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Hack and Roll: Game Over")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = 45
        self.lb_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 30, "Leaderboard")
        self.play_again_button = button.Button(button_width, button_height, button_x, button_y - 30, "Play Again")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.lb_button.is_pressed(pygame.mouse.get_pos()):
                        leaderboard.Leaderboard().run()
                    elif self.play_again_button.is_pressed(pygame.mouse.get_pos()):
                        runner.Runner().run()

            self.lb_button.draw(self.screen)
            self.play_again_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()