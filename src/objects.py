from pygame import Rect

from graphics import PlayerGFX


class Object(object):
    def __init__(self):
        pass


class Player(Object):
    speed = 6

    def __init__(self, left=100, top=100):
        super(Player, self).__init__()

        self.rect = Rect(
            (left, top),
            (80, 80))

        self.gfx = PlayerGFX(self.rect)
