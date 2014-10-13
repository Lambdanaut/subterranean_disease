from pygame import Rect

from graphics import PlayerGFX
from util import add_vectors


class Object(object):
    def __init__(self):
        pass

class Lifeform(Object):
    max_speed = 6

    def __init__(self):
        self.vel   = (0, 0)
        self.accel = (0, 0)

    def update(self):
        self.update_vel()
        self.update_pos()

    def update_pos(self):
    	new_pos = add_vectors((self.rect.left, self.rect.top), self.vel)
    	self.rect.left = new_pos[0]
    	self.rect.top = new_pos[1]

    def update_vel(self):
        self.vel = add_vectors(self.vel, self.accel)

    def update_accel(self, move_vector):
        self.accel = add_vectors(self.accel, move_vector)


class Player(Lifeform):
    def __init__(self, left=100, top=100):
        super(Player, self).__init__()

        self.rect = Rect(
            (left, top),
            (80, 80))

        self.gfx = PlayerGFX(self.rect)
