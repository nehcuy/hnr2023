import pygame
import button
import main
from . import constants

class Leaderboard:

    def __init__(self):
        pygame.init()

        # state for leaderboard
        self.leaderboard = []

        # populate leaderboard if file exists
        try:
            with open(constants.LEADERBOARD_FILE, 'r') as f:
                for line in f:
                    player = line.split('-+-')
                    self.leaderboard.append((player[0], int(player[1]), int(player[2]), int(player[3])))
                self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
                self.leaderboard = self.leaderboard[:5]
        except FileNotFoundError:
            pass

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Leaderboard")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = self.screen.get_height() - 50
        self.main_menu_button = button.Button(button_width + 20, button_height, button_x - 10, button_y - 30, "Main Menu")

    def add_score(self, name, score, time_elapsed, obstacles_destroyed):
        self.leaderboard.append((name, score, time_elapsed, obstacles_destroyed))
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:5]

    def save_leaderboard(self):
        with open(constants.LEADERBOARD_FILE, 'w+') as f:
            for player in self.leaderboard:
                f.write(player[0] + '-+-' + str(player[1]) + '-+-' + str(player[2]) + '-+-' + str(player[3]) + '\n')

    def run(self):
        running = True
        self.screen.fill(constants.GREY)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_leaderboard()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_menu_button.is_pressed(pygame.mouse.get_pos()):
                        main.Main().run()

            # draw leaderboard with back button
            font = pygame.font.SysFont('couriernew', 16)
            main_header_font = pygame.font.SysFont('couriernew', 24)
            lb_header_text = main_header_font.render('Leaderboard', True, (255, 255, 255))
            self.screen.blit(lb_header_text, (self.screen.get_width() / 2 - lb_header_text.get_width() / 2, 15))
            name_header_text = font.render('Name', True, (255, 255, 255))
            score_header_text = font.render('Score', True, (255, 255, 255))
            time_header_text = font.render('Time Elapsed', True, (255, 255, 255))
            obstacles_header_text = font.render('Obstacles Destroyed', True, (255, 255, 255))
            total_width = 150 + name_header_text.get_width() + score_header_text.get_width() + time_header_text.get_width() + obstacles_header_text.get_width()
            gap_between_headers = 50
            self.screen.blit(name_header_text, (self.screen.get_width() / 2 - total_width / 2, 50))
            self.screen.blit(score_header_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + gap_between_headers, 50))
            self.screen.blit(time_header_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + score_header_text.get_width() + gap_between_headers * 2, 50))
            self.screen.blit(obstacles_header_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + score_header_text.get_width() + time_header_text.get_width() + gap_between_headers * 3, 50))

            for index, player in enumerate(self.leaderboard):
                name_text = font.render(player[0], True, (255, 255, 255))
                score_text = font.render(str(player[1]) + ' pt', True, (255, 255, 255))
                time_text = font.render(str(player[2]) + ' seconds', True, (255, 255, 255))
                obstacles_text = font.render(str(player[3]) + ' obstacles', True, (255, 255, 255))
                self.screen.blit(name_text, (self.screen.get_width() / 2 - total_width / 2, 80 + index * 30))
                self.screen.blit(score_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + gap_between_headers, 80 + index * 30))
                self.screen.blit(time_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + score_header_text.get_width() + gap_between_headers * 2, 80 + index * 30))
                self.screen.blit(obstacles_text, (self.screen.get_width() / 2 - total_width / 2 + name_header_text.get_width() + score_header_text.get_width() + time_header_text.get_width() + gap_between_headers * 3, 80 + index * 30))
            self.main_menu_button.draw(self.screen)

            # erase text when back button is pressed
            if not running:
                self.screen.fill((0, 0, 0))

            pygame.display.flip()
        pygame.display.flip()