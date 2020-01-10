from character.Player import *
from vector.Vector import *
from color.Color import *
from settings.Settings import screen_width, screen_height, platform_width, platform_height
from surface.Surface import Surface
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([screen_width, screen_height])
        self.__clock = pygame.time.Clock()
        self.__player = Player(self.__screen, Vector(0, 0), 50, 50)
        self.__finish = Surface(self.__screen, Vector(2400, 200), platform_width, platform_height)
        self.__platform = (Surface(self.__screen, Vector(20, 240), platform_width, platform_height),
                           Surface(self.__screen, Vector(640, 300), platform_width, platform_height),
                           Surface(self.__screen, Vector(940, 240), platform_width, platform_height),
                           Surface(self.__screen, Vector(1340, 300), platform_width, platform_height),
                           Surface(self.__screen, Vector(1640, 460), platform_width, platform_height),
                           Surface(self.__screen, Vector(2000, 300), platform_width, platform_height))

    def get_display_size(self):
        return self.__screen

    @staticmethod
    def __quit_program():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        for single in self.__platform:
            if self.__player.get_rect().colliderect(single.get_rect()):
                self.__player.vector.y = single.vector.y - self.__player.height
        self.__player.update()

    def draw_player(self):
        self.__player.draw()

    def draw_platform(self):
        for single in self.__platform:
            single.draw()

    def draw_finish(self):
        self.__finish.draw()

    def win(self):
        if self.__player.get_rect().colliderect(self.__finish.get_rect()):
            print("You have won!")
            quit()

    def run(self):

        run_game = True
        while run_game:

            run_game = self.__quit_program()

            self.__screen.fill(color_background)
            self.win()
            self.update()
            self.draw_player()
            self.draw_platform()
            self.draw_finish()
            pygame.display.update()
            self.__clock.tick(500)  # Framerate

            keys = pygame.key.get_pressed()
            if self.__player.vector.x > 900:
                if keys[pygame.K_RIGHT]:
                    self.__finish.vector.x -= 1
                    for single in self.__platform:
                        single.vector.x -= 1
                        self.__player.vector.x = 900

            if self.__player.vector.x < 200:
                if keys[pygame.K_LEFT]:
                    self.__finish.vector.x += 1
                    for single in self.__platform:
                        single.vector.x += 1
                        self.__player.vector.x = 200

        quit()


game = Game()
game.run()
