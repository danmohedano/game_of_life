from data import Board
from camera import Camera
from config import *
import pygame
from pygame.locals import *
import time

# Constants for game loop
STOP = 0
PAUSE_RESUME = -1
CONTINUE = 1


def game_loop(board: Board, camera: Camera, run_flag: int):
    """Manage game loop.

    Args:
        board (Board): Board to display
        camera (Camera): Camera to display the board
        run_flag (int): Flag with the state of the execution
    """
    if run_flag > 0:
        board.iterate()
    camera.display()

    pygame.display.update()


def input(camera: Camera):
    """Manage user inputs.
    
    Args:
        camera (Camera): The camera to display the board
    """
    out = CONTINUE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close command
            return STOP
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
            elif event.key == pygame.K_z:
                # More zoom
                camera.zoom_update(0.25)
            elif event.key == pygame.K_x:
                # Less zoom
                camera.zoom_update(-0.25)
            elif event.key == pygame.K_SPACE:
                # Pause/resume
                out = PAUSE_RESUME
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed(3)
            if pressed[0]:
                if DEBUG:
                    print('Clicked at coordinates', pygame.mouse.get_pos())
                mouse_x, mouse_y = pygame.mouse.get_pos()
                camera.activate(mouse_x, mouse_y)

    return out


def main():
    # Initialization
    pygame.init()
    board = Board(GRID_SIZE, GRID_SIZE)

    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    camera = Camera(board, screen)
    pygame.display.set_caption('Game of Life')
    run_flag = PAUSE_RESUME

    # Load the board
    board.load(FILE)

    # Show initial state
    camera.display()
    time.sleep(1)

    # Game loop
    while run_flag != STOP:
        run_flag *= input(camera)
        game_loop(board, camera, run_flag)

    pygame.quit()


if __name__ == '__main__':
    main()
