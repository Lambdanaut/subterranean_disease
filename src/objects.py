from pygame import Rect

from graphics import PlayerGFX, WallGFX, NpcGFX
from settings import VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT
from util import Vec2d


class Object(object):
    obj_type = None
    orientation = 0

    def __init__(self):
        pass


class Wall(Object):
    obj_type = 'env'
    def __init__(self, left, top):
        super(Wall, self).__init__()

        self.rect = Rect(
            (left, top),
            (VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT))

        self.gfx = WallGFX(self)


class Lifeform(Object):
    obj_type = 'npc'

    max_vel = Vec2d(10, 10)
    friction = 0.9

    def __init__(self, left, top):
        super(Lifeform, self).__init__()

        self.rect = Rect(
            (left, top),
            (60, 50))

        self.vel = Vec2d(0, 0)

    def update(self, walls):
        self.update_friction()
        self.update_pos(walls)

    def update_pos_axis(self, dx, dy, walls):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def update_pos(self, walls):
        if self.vel.x != 0:
            self.update_pos_axis(self.vel.x, 0, walls)
        if self.vel.y != 0:
            self.update_pos_axis(0, self.vel.y, walls)

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
    obj_type='player'
    def __init__(self, left, top):
        super(Player, self).__init__(left, top)

        self.gfx = PlayerGFX(self)


class NPC(Lifeform):
    def __init__(self, left, top):
        super(NPC, self).__init__(left, top)

        self.gfx = NpcGFX(self)
