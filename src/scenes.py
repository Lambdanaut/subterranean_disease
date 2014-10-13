from abc import ABCMeta, abstractmethod
import math
import sys

import pygame
from pygame.locals import *

from objects import Player


class Scene(object):
    @abstractmethod
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def main_loop(self):
        pass

    @abstractmethod
    def get_player_input(self):
        pass


class Menu(Scene):
    def __init__(self, game):
        super(Menu, self).__init__(game)

    def get_player_input(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or key[K_ESCAPE]:
                pygame.quit()
                sys.exit()


class Ingame(Scene):
    def __init__(self, game):
        super(Ingame, self).__init__(game)

        self.h = Player()

    def main_loop(self):
        self.get_player_input()
        self.calculate()
        self.draw()

    def get_player_input(self):
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or key[K_ESCAPE]:
                pygame.quit()
                sys.exit()

            # Player movement
            elif event.type == KEYDOWN:
                pass
                # if (event.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]):

        # Player orientation
        (mx, my) = pygame.mouse.get_pos()

        self.h.gfx.d = \
            math.degrees(math.atan2(mx - self.h.rect.left, my - self.h.rect.top))

        to_move_x = 0
        to_move_y = 0
        if key[K_UP]:
            to_move_y -= 5
        if key[K_RIGHT]:
            to_move_x += 5
        if key[K_DOWN]:
            to_move_y += 5
        if key[K_LEFT]:
            to_move_x -= 5

        if to_move_x or to_move_y:
            self.h.gfx.state = 'walking'
            self.h.rect.top += to_move_y
            self.h.rect.left += to_move_x
        else:
            self.h.gfx.state = 'neutral'

    def calculate(self):
        self.calculate_player()
        self.calculate_npc()
        self.calculate_env()

    def draw(self):
        self.game.screen.surface.fill(Color(0,0,0))
        self.draw_player()
        self.draw_npc()
        self.draw_env()
        pygame.display.update()

    def calculate_player(self):
        pass

    def calculate_npc(self):
        pass

    def calculate_env(self):
        pass

    def draw_env(self):
        pass

    def draw_npc(self):
        pass

    def draw_player(self):
        self.h.gfx.draw(self.game.screen.surface)
        pass

