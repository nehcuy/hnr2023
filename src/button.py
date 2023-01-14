import pygame

class Button:
    def __init__(self, width, height, x, y, text):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.button = pygame.Surface((self.width, self.height))
        self.button.fill(self.color)
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = self.font.render(text, True, (255, 255, 255))
    
    def draw(self, screen):
        screen.blit(self.button, (self.x, self.y))
        screen.blit(self.text, (self.x + (self.width - self.text.get_width())/2, self.y + (self.height - self.text.get_height())/2))
    
    def is_pressed(self, mouse_pos):
        return (self.x <= mouse_pos[0] <= self.x + self.width) and (self.y <= mouse_pos[1] <= self.y + self.height)