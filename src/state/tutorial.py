import pygame
import button
import main
import os

import state.constants as c

class Tutorial:
    def __init__(self, leaderboard):
        self.leaderboard = leaderboard
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Hack and Roll: Tutorial")

        # Create the button
        button_width = 100
        button_height = 50
        button_x = (self.screen.get_width() / 2) - (button_width / 2)
        button_y = self.screen.get_height() - button_height - 10
        self.back_button = button.Button(button_width, button_height, button_x, button_y, "Back")

        # Image of obstacles
        self.obstacle_image = [pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Tree.png")),
                                 pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Rock.png")),
                                 pygame.image.load(os.path.join(c.APP_FOLDER, "images", "obstacles", "Spike.png"))]

    def display_upper_half(self, font):
        # Display the tutorial text
            text = font.render("W / Up Arrow Key: Move to lane on top", True, c.BLACK)
            text_rect = text.get_rect()
            text_rect.left = c.TUTORIAL_TEXT_SPACING
            text_rect.top = c.TUTORIAL_TEXT_SPACING
            self.screen.blit(text, text_rect)
            text = font.render("A / Left Arrow Key: Roll", True, c.BLACK)
            text_rect.top += c.TUTORIAL_TEXT_SPACING
            self.screen.blit(text, text_rect)
            text = font.render("S / Down Arrow Key: Move to lane below", True, c.BLACK)
            text_rect.top += c.TUTORIAL_TEXT_SPACING
            self.screen.blit(text, text_rect)
            text = font.render("D / Right Arrow Key: Chop", True, c.BLACK)
            text_rect.top += c.TUTORIAL_TEXT_SPACING
            self.screen.blit(text, text_rect)

            pygame.draw.rect(self.screen, c.BLACK, pygame.Rect(0, c.SCREEN_HEIGHT / 2 - c.TUTORIAL_TEXT_SPACING * 2, c.SCREEN_WIDTH, 5))

    def display_lower_half(self, font):
        tree = self.obstacle_image[0]
        rock = self.obstacle_image[1]
        spike = self.obstacle_image[2]
        tree = pygame.transform.smoothscale(tree, (40, 40))
        rock = pygame.transform.smoothscale(rock, (40, 40))
        spike = pygame.transform.smoothscale(spike, (45, 45))

        self.screen.blit(tree, (c.TUTORIAL_TEXT_SPACING, c.SCREEN_HEIGHT / 2 - c.TUTORIAL_TEXT_SPACING))
        text = font.render("Chop the tree down or change lanes to dodge!", True, c.BLACK)
        text_rect = text.get_rect()
        text_rect.top = c.SCREEN_HEIGHT / 2 - c.TUTORIAL_TEXT_SPACING + 5
        text_rect.left = c.TUTORIAL_TEXT_SPACING + 20 + c.TUTORIAL_TEXT_SPACING
        self.screen.blit(text, text_rect)

        self.screen.blit(rock, (c.TUTORIAL_TEXT_SPACING, c.SCREEN_HEIGHT / 2 + c.TUTORIAL_TEXT_SPACING - 15))
        text = font.render("Roll over the rock or change lanes to dodge!", True, c.BLACK)
        text_rect.top += c.TUTORIAL_TEXT_SPACING * 2 - 10
        self.screen.blit(text, text_rect)

        self.screen.blit(spike, (c.TUTORIAL_TEXT_SPACING, c.SCREEN_HEIGHT / 2 + c.TUTORIAL_TEXT_SPACING * 3 - 36))
        text = font.render("Escape by only changing lanes!", True, c.BLACK)
        text_rect.top += c.TUTORIAL_TEXT_SPACING * 2 - 10
        self.screen.blit(text, text_rect)

        font = pygame.font.SysFont('couriernew', 16)
        text = font.render("Hint: You can hold down on the hack/roll buttons to make things easier.", True, c.BLACK)
        text_rect.top += c.TUTORIAL_TEXT_SPACING * 2 - 20
        text_rect.left = c.TUTORIAL_TEXT_SPACING
        self.screen.blit(text, text_rect)

        text = font.render("Hint: You earn more points hacking & rolling obstacles >:)", True, c.BLACK)
        text_rect.top += c.TUTORIAL_TEXT_SPACING * 2 - 50
        self.screen.blit(text, text_rect)
        
    def run(self):
        running = True
        while running:
            self.screen.fill(c.GREY)
            font = pygame.font.SysFont('couriernew', 25)       
            self.display_upper_half(font)
            self.display_lower_half(font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_pressed(pygame.mouse.get_pos()):
                        main.Main().run()

            self.back_button.draw(self.screen)
            pygame.display.flip()
        pygame.quit()