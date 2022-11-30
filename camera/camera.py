import pygame
from data import Board
from .constants import CELL_COLOR, GRID_COLOR
from config import DEBUG


class Camera:
    """
    Camera class reponsible for the diplay of the board every DELAY ms
    """

    def __init__(self, board: Board, screen: pygame.Surface):
        """Constructor method for the camera
        
        Args:
            board (Board): Board to display
            screen (pygame.Surface): Screen where to display the board
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
        """Displays the current board state"""
        self.screen.fill(CELL_COLOR[0])

        # Calculate which cells are visible with the current state of the camera
        min_i = max(0, (int)((-1) * self.offsetX / (self.square_size * self.zoom))) 
        max_i = min(self.board.sizeX, (int)((self.screen_width - self.offsetX) / (self.square_size * self.zoom) + 1)) 
        min_j = max(0, (int)((-1) * self.offsetY / (self.square_size * self.zoom))) 
        max_j = min(self.board.sizeX, (int)((self.screen_height - self.offsetY) / (self.square_size * self.zoom) + 1)) 

        # Only display visible cells
        for x in range(min_i, max_i):
            for y in range(min_j, max_j):
                self.screen.fill(GRID_COLOR, (x * self.square_size * self.zoom + self.offsetX,
                                              y * self.square_size * self.zoom + self.offsetY,
                                              self.square_size * self.zoom,
                                              self.square_size * self.zoom))
                self.screen.fill(CELL_COLOR[int(self.board.next[x][y])],
                                 (x * self.square_size * self.zoom + 1 + self.offsetX,
                                  y * self.square_size * self.zoom + 1 + self.offsetY,
                                  self.square_size * self.zoom - 2,
                                  self.square_size * self.zoom - 2))

    def move(self, move_horizontal: int = 0, move_vertical: int = 0):
        """Move the camera
        
        Args:
            move_horizontal (int): if want to move the camera horizontally
            move_vertical (int): if want to move the camera vertically
        """
        self.offsetX += move_horizontal
        self.offsetY += move_vertical

    def zoom_update(self, zoom_increment: int = 0):
        """Update the zoom of the camera

        Args:
            zoom_increment (int): increment to the current zoom
        """
        self.zoom += zoom_increment
        if self.zoom < 0:
            self.zoom = 0

    def activate(self, mouse_x: int, mouse_y: int):
        """Processes the mouse input to activate a cell manually

        Args:
            mouse_x (int): x position of the mouse pointer on click
            mouse_y (int): y position of the mouse pointer on click
        """
        x_index = int((mouse_x - self.offsetX) // (self.square_size * self.zoom))
        y_index = int((mouse_y - self.offsetY) // (self.square_size * self.zoom))
        if x_index < self.board.sizeX and y_index < self.board.sizeY:
            self.board.next[x_index][y_index] = (self.board.next[x_index][y_index] + 1) % 2
