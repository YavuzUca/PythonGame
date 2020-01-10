from color.Color import *
from settings.Settings import screen_height, screen_width
from character.CharacterBase import Base
import pygame


class Player(Base):
    def __init__(self, screen, vector, height, width):
        super().__init__(screen, vector, height, width)
        self.alive = True

    def is_collided_with(self, platform):
        return self.rect.colliderect(platform.rect)

    def update(self):
        if self.alive:
            self.get_gravity()

            keys = pygame.key.get_pressed()
            r_border = screen_width - self.width
            b_border = screen_height - self.height
            if keys[pygame.K_LEFT]:
                self.vector.x -= 1
                if self.vector.x < 0:
                    self.vector.x = 0
            if keys[pygame.K_RIGHT]:
                self.vector.x += 1
                if self.vector.x > r_border:
                    self.vector.x = r_border
            if keys[pygame.K_SPACE]:
                self.vector.y -= 2
            if self.vector.y < 0:
                self.vector.y = 0
            if self.vector.y > b_border:
                print("You lost")
                quit()

    def draw(self):
        if self.alive:
            pygame.draw.rect(self.screen, color_rect, pygame.Rect(self.vector.x, self.vector.y, self.height, self.width))

    @staticmethod
    def get_draw():
        return pygame.draw

    def get_gravity(self):
        self.vector.y += 1
        return self
