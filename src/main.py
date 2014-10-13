import pygame, sys, os
if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'

from settings import GAME_NAME, GAME_AUTHOR, GAME_VERSION
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_FPS

import scenes


class Game(object):
    def __init__(self):
        #Init Pygame and Screen
        pygame.init()

        self.screen = self.Screen()
        self.clock = pygame.time.Clock()

        self.set_scene()
        self.main_loop()

    def set_scene(self, scene=None):
        self.scene = scene or scenes.Ingame(self)

    def main_loop(self):
        while True:
            self.scene.main_loop()
            self.clock.tick(SCREEN_FPS)

    class Screen(object):
        def __init__(self):
            self.width = SCREEN_WIDTH
            self.height = SCREEN_HEIGHT
            self.icon = self.Icon()

            self.surface = pygame.display.set_mode((self.width, self.height))

            pygame.display.set_caption(
                '{} - {} - v{}'.format(GAME_NAME, GAME_AUTHOR, GAME_VERSION))


        class Icon(object):
            def __init__(self):
                self.surface = pygame.Surface((1,1))

                self.surface.set_alpha(0)
                pygame.display.set_icon(self.surface)

