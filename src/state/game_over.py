import pygame
import button
import main
import state.constants as c

from . import runner

class GameOver:
    def __init__(self, leaderboard, score):
        self.leaderboard = leaderboard
        self.score = score
        self.leaderboard.add_score('Player', score)
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Game Over")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = 45
        self.lb_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 30, "Leaderboard")
        self.play_again_button = button.Button(button_width + 40, button_height, button_x - 20, button_y - 30, "Play Again")
        self.main_menu_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 90, "Main Menu")

    def run(self):
        running = True
        while running:
            self.screen.fill(c.GREY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.leaderboard.save_leaderboard()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.lb_button.is_pressed(pygame.mouse.get_pos()):
                        self.leaderboard.run()
                    elif self.play_again_button.is_pressed(pygame.mouse.get_pos()):
                        runner.Runner(self.leaderboard).run()
                    elif self.main_menu_button.is_pressed(pygame.mouse.get_pos()):
                        main.Main().run()

            self.play_again_button.draw(self.screen)
            self.lb_button.draw(self.screen)
            self.main_menu_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()