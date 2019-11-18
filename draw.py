import pygame
import images
pygame.font.init()

def __drawHiddenTile(screen, tile):
    r = __createRect(tile)
    screen.blit(images.hidden, r)

def __drawOpenTile(screen, tile):
    r = __createRect(tile)
    if tile.bomb:
        screen.blit(images.neighbours[0], r)
        screen.blit(images.bomb, r)
    else:
        img = images.neighbours[tile.neighbours]
        screen.blit(img, r)

def __drawFlagTile(screen, tile):
    r = __createRect(tile)
    screen.blit(images.flagged, r)

def drawTile(screen, tile):
    if tile.open:
        __drawOpenTile(screen, tile)
    elif tile.flag:
        __drawFlagTile(screen, tile)
    else:
        __drawHiddenTile(screen, tile)

def __createRect(tile):
    scale = 25
    return pygame.Rect(tile.x * scale, tile.y * scale, 
        (tile.x+1) * scale, (tile.y+1) * scale)

def drawEnd(screen, win, ww, wh):
    width = 80
    height = 40
    r = pygame.Rect(ww/2 - width/2, wh/2 - height/2, width, height)
    font = pygame.font.SysFont("Arial", 50)
    if win:
        pygame.draw.rect(screen, (200, 200, 0), r)
        text = pygame.transform.scale(
            font.render(" You won! ", True, (0,0,0)), (80,40))
        screen.blit(text, r)
    else:
        pygame.draw.rect(screen, (200, 0, 0), r)
        text = pygame.transform.scale(
            font.render(" You lost! ", True, (0,0,0)), (80,40))
        screen.blit(text, r)
    pygame.draw.rect(screen, (0, 0, 0), r, 3)
