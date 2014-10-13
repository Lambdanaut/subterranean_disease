import pygame
import pygame.gfxdraw as gfxdraw
from pygame import Color
from pygame import Rect

from settings import VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT
from settings import ANIMATION_LAG_2, ANIMATION_LAG_3, ANIMATION_LAG_4

NEUTRAL = 0
WALKING = 1

class GFX(object):
    def __init__(self, rect, state, lag):
        self.surface = pygame.Surface((VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT))

        self.state = state
        self.lag = lag

        self.frame = 0
        self.orientation = 0
        self.rect = rect

    def draw(self, screen):
        self.surf.fill((0,0,0))
        self.surf.set_colorkey((0, 0, 0))

        cur_frames = self.frames[self.state]
        cur_frame = cur_frames[(self.frame // self.lag)  % (len(cur_frames))]

        for rect, color in cur_frame:
            pygame.draw.rect(self.surf, color, rect)

        rotated_surf = pygame.transform.rotate(self.surf, self.orientation)

        rotated_rect = rotated_surf.get_rect()
        rotated_rect.center = (self.rect.left, self.rect.top)

        screen.blit(rotated_surf, rotated_rect)

        self.frame += 1

    def set_state(self, state=NEUTRAL):
        if self.state != state:
            self.frame = 0
            self.state = state

class HumanoidGFX(GFX):
    def __init__(self,
        rect,
        state=NEUTRAL,
        lag=ANIMATION_LAG_4,
        head_color=None,
        body_color=None,
        hair_color=None):

        super(HumanoidGFX, self).__init__(rect, state, lag)

        self.body_color = body_color or \
            Color(150, 25, 25)
        self.head_color = head_color or \
            Color(239, 208, 207)
        self.hair_color = hair_color or \
            Color(20, 50, 50)

        self.body1_rect = Rect(10, 20, 60, 40)
        self.body2_rect = Rect(10, 27, 60, 40)
        self.head1_rect = Rect(25, 45, 30, 30)
        self.head2_rect = Rect(25, 50, 30, 30)
        self.hair1_rect = Rect(25, 40, 30, 30)
        self.hair2_rect = Rect(25, 44, 30, 30)

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

        self.surf = pygame.Surface((80, 80))


class PlayerGFX(HumanoidGFX):
    pass
