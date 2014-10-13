from pygame import Rect

from graphics import PlayerGFX
from util import Vec2d


class Object(object):
    def __init__(self):
        pass


class Lifeform(Object):
    max_vel = Vec2d(10, 10)
    friction = 0.9

    def __init__(self):
        self.vel   = Vec2d(0, 0)

    def update(self):
        print(self.vel)
        self.update_friction()
        self.update_pos()

    def update_pos(self):
        new_pos = self.rect.topleft + self.vel
        self.rect.topleft = new_pos

    def update_vel(self, other_vector=None):
        if other_vector:
            self.vel += other_vector
            self.vel.restrain(self.max_vel)
        else:
            self.vel = Vec2d(0, 0)

    def update_friction(self):
        self.vel *= self.friction
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
        if abs(self.vel.y) < 0.5:
            self.vel.y = 0


class Player(Lifeform):
    def __init__(self, left=100, top=100):
        super(Player, self).__init__()

        self.rect = Rect(
            (left, top),
            (80, 80))

        self.gfx = PlayerGFX(self.rect)
