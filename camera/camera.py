import threading
import pygame
from data import Board, ALIVE, DEAD
from .constants import CELL_COLOR, GRID_COLOR
from config import DEBUG


class Camera:
    """
    Camera class reponsible for the diplay of the board every DELAY ms
    """

    def __init__(self, board: Board, screen: pygame.Surface):
        """
        Constructor method for the camera
        :param board: board to display
        :param screen: screen where to display the board
        """
        self.board = board
        self.screen = screen

        # Calculate values for display
        self.screen_width, self.screen_height = self.screen.get_size()
        self.square_size = min(self.screen_width / self.board.sizeX,
                               self.screen_height / self.board.sizeY)

        # Initiliaze config variables of the camera
        self.zoom = 1.0
        self.offsetX = 0.0
        self.offsetY = 0.0
        self.config_lock = threading.Semaphore()

        if DEBUG:
            print("Initialized camera")

    def display(self):
        """
        Displays the current board state
        """
        for x in range(self.board.sizeX):
            for y in range(self.board.sizeY):
                # TODO: display only viewed cells for performance increase
                self.screen.fill(GRID_COLOR, (y * self.square_size * self.zoom + self.offsetY,
                                              x * self.square_size * self.zoom + self.offsetX,
                                              self.square_size * self.zoom,
                                              self.square_size * self.zoom))
                self.screen.fill(CELL_COLOR[int(self.board.next[x][y])],
                                 (y * self.square_size * self.zoom + 1 + self.offsetY,
                                  x * self.square_size * self.zoom + 1 + self.offsetX,
                                  self.square_size * self.zoom - 2,
                                  self.square_size * self.zoom - 2))
