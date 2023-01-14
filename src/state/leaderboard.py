import pygame
import button

class Leaderboard:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Hack and Roll: Leaderboard")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = (self.screen.get_height() / 2) - (button_height / 2)
        self.back_button = button.Button(button_width, button_height, button_x, button_y - 30, "Back")
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_pressed(pygame.mouse.get_pos()):
                        running = False

            self.back_button.draw(self.screen)
            pygame.display.flip()
        pygame.display.flip()