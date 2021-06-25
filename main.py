from data import Board
from camera import Camera
from config import *
import pygame
from pygame.locals import *
import time
import threading


def game_loop(board: Board, camera: Camera):
    """
    Manage game loop
    :param board:
    :param camera:
    :return:
    """
    board.iterate()
    camera.display()

    pygame.display.update()


def input(camera: Camera):
    """
    Manage user inputs
    :param camera:
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close command
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Move camera to the left
                camera.move(SCR_WIDTH // 10, 0)
            elif event.key == pygame.K_RIGHT:
                # Move camera to the right
                camera.move(-SCR_WIDTH // 10, 0)
            elif event.key == pygame.K_UP:
                # Move camera up
                camera.move(0, SCR_HEIGHT // 10)
            elif event.key == pygame.K_DOWN:
                # Move camera down
                camera.move(0, -SCR_HEIGHT // 10)
            elif event.key == pygame.K_PAGEUP:
                # More zoom
                camera.zoom_update(0.25)
            elif event.key == pygame.K_PAGEDOWN:
                # Less zoom
                camera.zoom_update(-0.25)

    return True


def main():
    # Initialization
    pygame.init()
    board = Board(GRID_SIZE, GRID_SIZE)
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    camera = Camera(board, screen)
    pygame.display.set_caption('Game of Life')
    run_flag = True

    # Load the board
    board.load(FILE)

    # Show initial state
    camera.display()
    time.sleep(1)

    # Game loop
    while run_flag:
        run_flag = input(camera)
        game_loop(board, camera)

    pygame.quit()


if __name__ == '__main__':
    main()
