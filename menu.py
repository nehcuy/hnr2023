import pygame
from button import Button

# create simple menu with play and exit button
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.play_button = Button(self, "Play")
        self.exit_button = Button(self, "Exit")

    def draw_menu(self):
        self.screen.fill(self.bg_color)
        self.play_button.draw_button()
        self.exit_button.draw_button()

    def is_start_pressed(self):
        # get mouse pos x and y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # check if mouse is on play button
        return self.play_button.is_start_button() and pygame.mouse.get_pressed()[0]

