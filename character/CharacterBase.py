import pygame


class Base:
    def __init__(self, screen, vector, width, height):
        self.screen = screen
        self.vector = vector
        self.width = width
        self.height = height

    def get_rect(self):
        return pygame.Rect(self.vector.x, self.vector.y, self.width, self.height)