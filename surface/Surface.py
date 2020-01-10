import pygame
from color.Color import color_rect


class Surface:
    def __init__(self, screen, vector, height, width):
        self.screen = screen
        self.vector = vector
        self.height = height
        self.width = width

    def draw(self):
        rect = self.vector.x, self.vector.y, self.height, self.width
        pygame.draw.rect(self.screen, color_rect, pygame.Rect(rect))

    def get_rect(self):
        return pygame.Rect(self.vector.x, self.vector.y, self.height, self.width)
