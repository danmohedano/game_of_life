import threading
import pygame
from data import Board
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
        # self.config_lock = threading.Semaphore()

        if DEBUG:
            print("Initialized camera")

    def display(self):
        """
        Displays the current board state
        """
        # with self.config_lock:
        self.screen.fill(CELL_COLOR[0])
        for x in range(self.board.sizeX):
            for y in range(self.board.sizeY):
                # TODO: display only viewed cells for performance increase
                self.screen.fill(GRID_COLOR, (x * self.square_size * self.zoom + self.offsetX,
                                              y * self.square_size * self.zoom + self.offsetY,
                                              self.square_size * self.zoom,
                                              self.square_size * self.zoom))
                self.screen.fill(CELL_COLOR[int(self.board.next[x][y])],
                                 (x * self.square_size * self.zoom + 1 + self.offsetX,
                                  y * self.square_size * self.zoom + 1 + self.offsetY,
                                  self.square_size * self.zoom - 2,
                                  self.square_size * self.zoom - 2))

    def move(self, move_horizontal=0, move_vertical=0):
        """
        Move the camera
        :param move_horizontal: if want to move the camera horizontally
        :param move_vertical: if want to move the camera vertically
        """
        self.offsetX += move_horizontal
        self.offsetY += move_vertical

    def zoom_update(self, zoom_increment=0):
        """
        Update the zoom of the camera
        :param zoom_increment: increment to the current zoom
        """
        self.zoom += zoom_increment
        if self.zoom < 0:
            self.zoom = 0

    def activate(self, mouse_x: int, mouse_y: int):
        """
        Processes the mouse input to activate a cell manually
        :param mouse_x: x position of the mouse pointer on click
        :param mouse_y: y position of the mouse pointer on click
        """
        x_index = int((mouse_x - self.offsetX) // (self.square_size * self.zoom))
        y_index = int((mouse_y - self.offsetY) // (self.square_size * self.zoom))
        if x_index < self.board.sizeX and y_index < self.board.sizeY:
            self.board.next[x_index][y_index] = (self.board.next[x_index][y_index] + 1) % 2
