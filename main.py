from data import Board
from camera import Camera
from config import *
import pygame
from pygame.locals import *
import time
import threading


def main():
    # Initialization
    pygame.init()
    board = Board(GRID_SIZE, GRID_SIZE)
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    camera = Camera(board, screen)
    pygame.display.set_caption('Game of Life')

    # Load the board
    board.load(FILE)

    # Show initial state
    camera.display()
    time.sleep(1)

    # Game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                run = False

        board.iterate()
        camera.display()

        pygame.display.update()
        pygame.time.delay(DELAY)

    pygame.quit()


if __name__ == '__main__':
    main()
