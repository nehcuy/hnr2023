import os
import pygame
import button
import state.runner
import state.leaderboard
import state.tutorial
import state.constants as c

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll")
        img = pygame.image.load(os.path.join(c.APP_FOLDER, "images", "icon.png"))
        pygame.display.set_icon(img)

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = (self.screen.get_height() / 2) - (button_height / 2)
        self.start_button = button.Button(button_width, button_height, button_x, button_y - 30, "Start")
        self.lb_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 30, "Leaderboard")
        self.tutorial_button = button.Button(button_width + 40, button_height, button_x - 20, button_y + 90, "Tutorial")
        self.leaderboard = state.leaderboard.Leaderboard()
        
    def run(self):
        running = True
        while running:
            self.screen.fill(c.GREY)

            # Display game title
            font = pygame.font.SysFont('couriernew', 64, bold=True)
            text = font.render("Hack and Roll", True, c.BLACK)
            self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 50))
            font = pygame.font.SysFont('couriernew', 36)
            text = font.render("Try and hit 100 points!", True, c.BLACK)
            self.screen.blit(text, (self.screen.get_width() / 2 - text.get_width() / 2, 150))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.leaderboard.save_leaderboard()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_pressed(pygame.mouse.get_pos()):
                        state.runner.Runner(self.leaderboard).run()
                    elif self.lb_button.is_pressed(pygame.mouse.get_pos()):
                        self.leaderboard.run()
                    elif self.tutorial_button.is_pressed(pygame.mouse.get_pos()):
                        state.tutorial.Tutorial(self.leaderboard).run()
                        
            self.start_button.draw(self.screen)
            self.lb_button.draw(self.screen)
            self.tutorial_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.run()