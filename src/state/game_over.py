import pygame
import button
import main
import state.constants as c

from . import runner

class GameOver:
    def __init__(self, leaderboard, score, time_elapsed, obstacles_destroyed):
        self.leaderboard = leaderboard
        self.score = score
        self.time_elapsed = time_elapsed
        self.obstacles_destroyed = obstacles_destroyed
        self.leaderboard.add_score('Player', score, time_elapsed, obstacles_destroyed)
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Game Over")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = (self.screen.get_height() / 2) - (button_height / 2)
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

            # Show text for score, time elapsed, and obstacles destroyed
            font = pygame.font.SysFont('couriernew', 30)
            score_text = font.render('Score: ' + str(self.score), True, c.BLACK)
            time_text = font.render('Time Elapsed: ' + str(self.time_elapsed), True, c.BLACK)
            obstacles_text = font.render('Obstacles Destroyed: ' + str(self.obstacles_destroyed), True, c.BLACK)
            self.screen.blit(score_text, (self.screen.get_width() / 2 - score_text.get_width() / 2, 10))
            self.screen.blit(time_text, (self.screen.get_width() / 2 - time_text.get_width() / 2, 40))
            self.screen.blit(obstacles_text, (self.screen.get_width() / 2 - obstacles_text.get_width() / 2, 70))

            self.play_again_button.draw(self.screen)
            self.lb_button.draw(self.screen)
            self.main_menu_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()