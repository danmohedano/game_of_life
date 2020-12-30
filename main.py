from gameoflife import Board
from gameoflife.constants import SIZE
import pygame
from pygame.locals import *
import time


def main():
    # Initialization
    pygame.init()
    board = Board(SIZE)
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption('Game of Life')

    # Load the board
    board.load()

    # Show initial state
    board.display(screen)
    time.sleep(1)

    # Game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                run = False

        board.iterate()
        board.display(screen)

        pygame.display.update()
        pygame.time.delay(10)

    pygame.quit()


if __name__ == '__main__':
    main()
