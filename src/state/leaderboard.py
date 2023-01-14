import pygame
import button


class Leaderboard:

    def __init__(self):
        pygame.init()

        # state for leaderboard
        self.leaderboard = [
            ('Player 1', 35), ('Player 2', 37), ('Player 3', 25),
            ('Player 4', 20), ('Player 5', 33)
        ]

        self.screen = pygame.display.set_mode((400, 100 + 5 * 30))
        pygame.display.set_caption("Hack and Roll: Leaderboard")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = 45
        self.back_button = button.Button(button_width, button_height, button_x, button_y - 30, "Back")

    def add_score(self, name, score):
        self.leaderboard.append((name, score))
        self.leaderboard.sort(key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:5]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_pressed(pygame.mouse.get_pos()):
                        running = False

            # draw leaderboard with back button
            font = pygame.font.SysFont('Courier', 30)
            for i in range(len(self.leaderboard[:5])):
                text = font.render(
                    self.leaderboard[i][0] + ' - ' + "{:02d}".format(self.leaderboard[i][1]), True, (255, 255, 255))
                self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 70 + i * 30))
            self.back_button.draw(self.screen)

            # erase text when back button is pressed
            if not running:
                self.screen.fill((0, 0, 0))

            pygame.display.flip()
        pygame.display.flip()