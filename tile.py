class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bomb = False
        self.flag = False
        self.neighbours = 0
        self.open = False
    
    def setBomb(self):
        self.bomb = True

    def setNeighbours(self, n):
        self.neighbours = n

    def openTile(self):
        if not self.flag:
            self.open = True
        return self.open

    def toggleFlag(self):
        if not self.open:
            self.flag = not self.flag

    def __str__(self):
        return f'Tile ({self.x},{self.y}), bomb: {self.bomb}'

    def __repr__(self):
        if self.bomb:
            return "Bomb"
        else:
            return "No bomb"
