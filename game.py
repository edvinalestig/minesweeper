from tile import Tile
import random
from math import floor

class Game():
    def __init__(self, width, height, bombs):
        if bombs >= width*height:
            raise ValueError("Too many bombs!")
        self.bombs  = bombs
        self.ended  = False
        self.win    = False
        self.width  = width
        self.height = height
        self.tiles  = []
        for i in range(height):
            self.tiles.append([Tile(x,i) for x in range(width)])
        self.createBombs(bombs)
        self.findNeighbours()

    def reset(self):
        self.__init__(self.width, self.height, self.bombs)

    # Creates n random bombs
    # Create random positions on the board
    # and add a bomb to the selected tiles
    def createBombs(self, n):
        bombs = []
        while len(bombs) < n:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if (x,y) not in bombs:
                bombs.append((x,y))

        for pos in bombs:
            self.tiles[pos[1]][pos[0]].setBomb()

    # Returns if a tile has a bomb or not
    def bomb(self, x, y):
        return self.tiles[y][x].bomb

    # Find the number of bombs nearby 
    # for displaying on the board
    def findNeighbours(self):
        x = 0
        while x < self.width:
            y = 0
            while y < self.height:
                n = 0

                for i in range(-1,2):
                    for j in range(-1, 2):
                        if (not x+i < 0) and (not y+j < 0):
                            try:
                                if self.bomb(x+i, y+j):
                                    n += 1
                            except IndexError:
                                pass
                self.tiles[y][x].setNeighbours(n)
                y += 1
            x += 1

    # Find a tile from mouse position
    def findTile(self, x, y):
        x = floor(x/25)
        y = floor(y/25)
        return self.tiles[x][y]

    # Open a tile (and maybe surrounding tiles)
    def openTile(self, tile):
        if tile.open:
            return
        if tile.openTile():
            if tile.neighbours == 0:
                # Open the surrounding tiles
                for i in range(-1,2):
                    for j in range(-1, 2):
                        if (not tile.y+i < 0) and (not tile.x+j < 0):
                            try:
                                self.openTile(self.tiles[tile.y+i][tile.x+j])
                            except IndexError:
                                pass
            if tile.bomb:
                self.ended = True
                for t in self:
                    if t.bomb:
                        t.open = True

    # You can win by either opening all tiles or flagging all bombs
    def checkWin(self):
        opened = True
        flagged = True
        for tile in self:
            if (not tile.open) and (not tile.bomb):
                opened = False
            if tile.bomb and not tile.flag:
                flagged = False
            if tile.flag and not tile.bomb:
                flagged = False

        if opened or flagged:
            self.ended = True
            self.win = True
            for tile in self:
                if not tile.bomb:
                    tile.open = True

    # Turn the board into a string
    # nicely formatted
    def __str__(self):
        out = ""
        for row in self.tiles:
            s = ""
            for tile in row:
                if tile.bomb:
                    s += " B "
                else:
                    s += " - "
            out += s + "\n"
        return out

    def __iter__(self):
        return GameIter(self)

# Class for iterating over all tiles in Game
class GameIter():
    def __init__(self, game):
        self._game = game
        self._x = 0
        self._y = 0
    
    def __next__(self):
        if self._y == self._game.height:
            raise StopIteration

        tile = self._game.tiles[self._y][self._x]
        self._x += 1
        if self._x == self._game.width:
            self._x = 0
            self._y += 1
        return tile
