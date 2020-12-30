import data
import pygame
from pygame.locals import *
import time
import sys


# Initialization
pygame.init()
SIZE = 150
dt = data.Board(SIZE)
dt.load()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Game of Life')

# Show initial state
dt.display(screen)
time.sleep(1)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            run = False

    dt.iterate()
    dt.display(screen)

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
