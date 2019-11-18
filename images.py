import pygame
from pygame.image import load
from pygame.transform import scale

neighbours = []
neighbours.append(scale(load("./images/0.png"), (25, 25)))
neighbours.append(scale(load("./images/1.png"), (25, 25)))
neighbours.append(scale(load("./images/2.png"), (25, 25)))
neighbours.append(scale(load("./images/3.png"), (25, 25)))
neighbours.append(scale(load("./images/4.png"), (25, 25)))
neighbours.append(scale(load("./images/5.png"), (25, 25)))
neighbours.append(scale(load("./images/6.png"), (25, 25)))
neighbours.append(scale(load("./images/7.png"), (25, 25)))
neighbours.append(scale(load("./images/8.png"), (25, 25)))

hidden  = scale(load("./images/hidden.png"), (25, 25))
flagged = scale(load("./images/flagged.png"), (25, 25))
bomb    = scale(load("./images/bomb.png"), (25, 25))