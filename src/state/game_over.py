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
        user_text = ''
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
                elif event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    # Unicode standard is used for string formation
                    elif event.key != pygame.K_RETURN:
                        user_text += event.unicode
                        user_text = user_text[:6]
                # check if enter pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(user_text) > 0:
                        self.leaderboard.add_score(user_text, self.score, self.time_elapsed, self.obstacles_destroyed)
                        self.leaderboard.save_leaderboard()
                        self.leaderboard.run()

            # Show text for score, time elapsed, and obstacles destroyed
            font = pygame.font.SysFont('couriernew', 30)
            score_text = font.render('Score: ' + str(self.score), True, c.BLACK)
            time_text = font.render('Time Elapsed: ' + str(self.time_elapsed), True, c.BLACK)
            obstacles_text = font.render('Obstacles Destroyed: ' + str(self.obstacles_destroyed), True, c.BLACK)
            self.screen.blit(score_text, (self.screen.get_width() / 2 - score_text.get_width() / 2, 10))
            self.screen.blit(time_text, (self.screen.get_width() / 2 - time_text.get_width() / 2, 40))
            self.screen.blit(obstacles_text, (self.screen.get_width() / 2 - obstacles_text.get_width() / 2, 70))

            add_to_lb_font = pygame.font.SysFont('couriernew', 20)
            add_to_lb_text = add_to_lb_font.render('Add to leaderboard? Just type your name and press enter.', True, c.BLACK)
            self.screen.blit(add_to_lb_text, (self.screen.get_width() / 2 - add_to_lb_text.get_width() / 2, 120))
            
            # create text box
            text_box = pygame.Rect(self.screen.get_width() / 2 - 100, 150, 200, 30)
            pygame.draw.rect(self.screen, c.BLACK, text_box, 2)

            # allow players to edit text in text_box
            font = pygame.font.SysFont('couriernew', 20)
            text = font.render(user_text, True, c.BLACK)
            self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 155))

            self.play_again_button.draw(self.screen)
            self.lb_button.draw(self.screen)
            self.main_menu_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()