import os

from pygame import Rect

from objects import Wall, NPC

from settings import MAPS_FILEPATH
from settings import VIDEO_TILE_WIDTH, VIDEO_TILE_HEIGHT


OBJECT_CHART = {
    ' ': None,
    '|': Wall,
    'n': NPC,
}

class Map(list):
    def __init__(self):
        self.map_text = None

        self.load()

    def parse(self, map_text):
        """
        Parses a list of strings to a list of game objects

        :param map_text: List of strings
        :return [Object]: List of game objects
        """
        self.map_text = map_text

        row = 0
        column = 0
        for line in map_text:
            column = 0

            for char in line:
                try:
                    converted_char = OBJECT_CHART[char]
                    if converted_char is not None:
                        left = column * VIDEO_TILE_WIDTH
                        top  = row * VIDEO_TILE_HEIGHT
                        converted_char = converted_char(left, top)
                        self.append(converted_char)
                except KeyError: pass
                column += 1

            row += 1

    def load(self):
        """Loads and parses the map from file"""
        filepath = os.path.join(MAPS_FILEPATH, self.map_filename)
        with open(filepath) as f:
            lines = f.read().split('\n')
            self.parse(lines)


class TestMap(Map):
    map_filename = 'test_map'


tm = TestMap()

print(tm)
