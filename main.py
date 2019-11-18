import sys
import pygame

import draw
from tile import Tile
from game import Game

width, height = 10, 7
bombs = 15
g = Game(width, height, bombs)

pygame.init()
size = (25 * width, 25 * height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")

while True:
    event = pygame.event.wait()
    t = event.type
    if t == pygame.QUIT:
        sys.exit()
    elif t == pygame.MOUSEBUTTONDOWN:
        if not g.ended:
            y, x = event.pos
            button = event.button
            tile = g.findTile(x, y)
            if button == 3:
                tile.toggleFlag()
            elif button == 1:
                g.openTile(tile)
    elif t == pygame.KEYDOWN:
        if g.ended:
            if event.key == 13:
                g.reset()

    g.checkWin()

    for tile in g:
        draw.drawTile(screen, tile)

    if g.ended:
        draw.drawEnd(screen, g.win, width*25, height*25)

    pygame.display.flip()

