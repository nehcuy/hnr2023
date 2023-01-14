import pygame
import button
from . import constants


class Leaderboard:

    def __init__(self):
        pygame.init()

        # state for leaderboard
        self.leaderboard = []

        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Leaderboard")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = 45
        self.back_button = button.Button(button_width, button_height, button_x, button_y - 30, "Back")

    def add_score(self, name, score):
        self.leaderboard.append((name, score))
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:5]

    def run(self):
        running = True
        self.screen.fill(constants.GREY)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_pressed(pygame.mouse.get_pos()):
                        running = False

            # draw leaderboard with back button
            font = pygame.font.SysFont('Courier', 30)
            for index, player in enumerate(self.leaderboard):
                text = font.render(
                    player[0] + ': ' + "{:02d}".format(player[1]), True, (255, 255, 255))
                self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 70 + index * 30))
            self.back_button.draw(self.screen)

            # erase text when back button is pressed
            if not running:
                self.screen.fill((0, 0, 0))

            pygame.display.flip()
        pygame.display.flip()