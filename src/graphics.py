import pygame
import pygame.gfxdraw as gfxdraw
from pygame import Color
from pygame import Rect

from settings import VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT
from settings import ANIMATION_LAG_2, ANIMATION_LAG_3, ANIMATION_LAG_4

NEUTRAL = 0
WALKING = 1


class GFX(object):
    def __init__(self, obj, state=NEUTRAL, lag=1):
        self.obj = obj
        self.state = state
        self.lag = lag

        self.frame = 0

    def draw(self, screen):
        self.surf.fill((0,0,0))
        self.surf.set_colorkey((0, 0, 0))

        if type(self.frames) == tuple:
            rect = self.frames[0]
            color = self.frames[1]
            s = pygame.Surface(rect.size)
            s.set_alpha(color.a)
            s.fill(color)
            self.surf.blit(s, rect.topleft)

        elif type(self.frames) == dict:
            cur_frames = self.frames[self.state]
            cur_frame = cur_frames[(self.frame // self.lag)  % (len(cur_frames))]

            for rect, color in cur_frame:
                s = pygame.Surface(rect.size)
                s.set_alpha(color.a)
                s.fill(color)
                self.surf.blit(s, rect.topleft)

        rotated_surf = pygame.transform.rotate(self.surf, self.obj.orientation)

        rotated_rect = rotated_surf.get_rect()
        rotated_rect.center = self.obj.rect.center

        screen.blit(rotated_surf, rotated_rect)

        self.frame += 1

    def set_state(self, state=NEUTRAL):
        if self.state != state:
            self.frame = 0
            self.state = state


class WallGFX(GFX):
    def __init__(self,
        obj,
        wall_color=None):

        super(WallGFX, self).__init__(obj)

        self.wall_color = wall_color or \
            Color(15, 15, 15)

        self.wall_rect = Rect(0, 0, VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT)

        self.frames = (self.wall_rect, self.wall_color)

        self.surf = pygame.Surface((VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT))


class HumanoidGFX(GFX):
    def __init__(self,
        obj,
        state=NEUTRAL,
        lag=ANIMATION_LAG_4,
        head_color=None,
        body_color=None,
        hair_color=None):

        super(HumanoidGFX, self).__init__(obj, state, lag)

        self.body_color = body_color or \
            Color(150, 25, 25)
        self.head_color = head_color or \
            Color(239, 208, 207)
        self.hair_color = hair_color or \
            Color(20, 50, 50)

        self.body1_rect = Rect(0, 0, 60, 40)
        self.body2_rect = Rect(0, 7, 60, 40)
        self.head1_rect = Rect(15, 26, 30, 30)
        self.head2_rect = Rect(15, 29, 30, 30)
        self.hair1_rect = Rect(15, 20, 30, 30)
        self.hair2_rect = Rect(15, 25, 30, 30)

        self.frames = {
            NEUTRAL: [
                [
                    (self.body1_rect, self.body_color),
                    (self.head1_rect, self.head_color),
                    (self.hair1_rect, self.hair_color),
                ],
            ],
            WALKING: [
                [
                    (self.body1_rect, self.body_color),
                    (self.head1_rect, self.head_color),
                    (self.hair1_rect, self.hair_color),
                ],
                [
                    (self.body2_rect, self.body_color),
                    (self.head2_rect, self.head_color),
                    (self.hair2_rect, self.hair_color),
                ],
            ],
        }

        self.surf = pygame.Surface((60, 60))


class PlayerGFX(HumanoidGFX):
    pass


class NpcGFX(HumanoidGFX):
    def __init__(self, obj, *args, **kwargs):
        head_color = Color(50, 200, 50)
        body_color = Color(50, 50, 50)
        super(NpcGFX, self).__init__(
            obj,
            head_color=head_color,
            body_color=body_color) 

