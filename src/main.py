import pygame
import button
import state.runner

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Hack and Roll")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = (self.screen.get_height() / 2) - (button_height / 2)
        self.start_button = button.Button(button_width, button_height, button_x, button_y - 30, "Start")
        self.lb_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 30, "Leaderboard")
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_pressed(pygame.mouse.get_pos()):
                        state.runner.Runner().run()
                    elif self.lb_button.is_pressed(pygame.mouse.get_pos()):
                        print("Leaderboard")
                        
            self.start_button.draw(self.screen)
            self.lb_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.run()