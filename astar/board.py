from astar.astar import astar
from astar.show import show
from astar.depth import depth
from astar.dijkstra import dijkstra


class Board:
    def __init__(self, tile_size=100, algo=3, start_character='A', end_character='B', board='', tile_config='', font_size=16, tile_margin=0):
        self.tile_size = tile_size
        self.tiles = [[]]
        self.algo = algo
        self.start_character = start_character
        self.end_character = end_character
        self.board = board
        self.tile_config = tile_config
        self.font_size = font_size
        self.tile_margin = tile_margin

    def generate_tiles(self):
        self.tiles = [[Tile(board=self, x=x, y=y) for x in range(self.width)] for y in range(self.height)]

    def solve(self):
        if self.algo == 0:
            return astar(self)
        elif self.algo == 1:
            return dijkstra(self)
        elif self.algo == 2:
            return depth(self)
        elif self.algo == 3:
            return show(self)

    @property
    def tile_set(self):
        return set([a for b in self.tiles for a in b])

    @property
    def pixel_width(self):
        return self.width * self.tile_size

    @property
    def pixel_height(self):
        return self.height * self.tile_size

    @property
    def width(self):
        return max(max(map(len, self.tiles)), max(map(len,self.board.split('\n')))-1)

    @property
    def height(self):
        return max(len(self.tiles), self.board.count('\n')+1)

    def hex_config(self):
        colors = {
            'red': '#db2828',
            'orange': '#f2711c',
            'yellow': '#fbbd08',
            'olive': '#b5cc18',
            'green': '#21ba45',
            'teal': '#00b5ad',
            'blue': '#2185d0',
            'violet': '#6435c9',
            'purple': '#a333c8',
            'pink': '#e03997',
            'brown': '#a5673f',
            'grey': '#767676',
            'black': '#1b1c1d',
        }
        newconfig = self.tile_config
        for a in colors:
            newconfig  = newconfig.replace(a, colors[a])
        return newconfig

    def init(self):
        hex_config = self.hex_config()
        conf = {}
        if self.tile_config:
            lines = [a.strip() for a in hex_config.strip().split('\n')]
            for line in lines:
                conf[line.split(':')[0]] = line.split(':')[1].split(',')
        rows = [a.strip() for a in self.board.strip().split('\n')]
        self.generate_tiles()
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                try:
                    self.tiles[y][x].color = conf[c][1]
                except Exception:
                    self.tiles[y][x].color = '#2185d0'
                try:
                    self.tiles[y][x].weight = int(conf[c][0])
                except Exception:
                    self.tiles[y][x].weight = 1
                try:
                    self.tiles[y][x].character = c
                except Exception:
                    self.tiles[y][x].character = ''
        return self


class Tile:
    def __init__(self, board=None, x=0, y=0, weight=1, color='#2196f3', character=''):
        self.board = board
        self.x = x
        self.y = y
        self.weight = weight
        self.color = color
        self.character = character
        self.parent = None
        self.children = []
        self.g = 1000000
        self.h = 1000000

    @property
    def f(self):
        return self.g + self.h

    @property
    def x_start(self):
        return self.x + 1

    @property
    def y_start(self):
        return self.y + 1

    @property
    def x_end(self):
        return self.x + 2

    @property
    def y_end(self):
        return self.y + 2