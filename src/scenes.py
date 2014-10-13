from abc import ABCMeta, abstractmethod
import math
import sys

import pygame
from pygame.locals import *

from graphics import NEUTRAL, WALKING
from objects import Player
from settings import MOVE_UP, MOVE_RIGHT, MOVE_DOWN, MOVE_LEFT


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

        self.p = Player()

    def main_loop(self):
        self.get_player_input()
        self.calculate()
        self.draw()

    def get_player_input(self):
        # New input events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Player movement events
            elif event.type == KEYDOWN:
                if event.key == MOVE_UP or event.key == MOVE_RIGHT or event.key == MOVE_DOWN or event.key == MOVE_LEFT:
                    self.p.gfx.set_state(WALKING)


        # Player orientation
        (mx, my) = pygame.mouse.get_pos()

        self.p.gfx.orientation = \
            math.degrees(math.atan2(mx - self.p.rect.left, my - self.p.rect.top))

        key = pygame.key.get_pressed()

        # Player movement
        to_move_x = 0
        to_move_y = 0
        if key[MOVE_UP]:
            to_move_y -= 1
        if key[MOVE_RIGHT]:
            to_move_x += 1
        if key[MOVE_DOWN]:
            to_move_y += 1
        if key[MOVE_LEFT]:
            to_move_x -= 1

        if to_move_x or to_move_y:
            self.p.update_accel((to_move_x, to_move_y))
        else:
            self.p.gfx.set_state(NEUTRAL)

        # TODO: Menu
        if key[K_ESCAPE]:
            pygame.quit()
            sys.exit()

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
        self.p.update()

    def calculate_npc(self):
        pass

    def calculate_env(self):
        pass

    def draw_env(self):
        pass

    def draw_npc(self):
        pass

    def draw_player(self):
        self.p.gfx.draw(self.game.screen.surface)
        pass
