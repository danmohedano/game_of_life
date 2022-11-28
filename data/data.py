import threading
import numpy as np
import pygame
import random
from .constants import ALIVE, DEAD
from config import DEBUG


class Board:
    def __init__(self, size_x: int, size_y: int):
        """Constructor method for the board.

        Args:
            size_x (int): Width of the board
            size_y (int): Height of the board
        """
        self.sizeX = size_x
        self.sizeY = size_y
        self.current = np.zeros((size_y, size_x))
        self.next = np.zeros((size_y, size_x))
        self.iteration = 0

        if DEBUG:
            print(f"Initialized board [size=({self.sizeX},{self.sizeY})]") 

    def iterate(self):
        """Calculates an iteration for the board

        It first swaps the boards and calculates the new next board.
        """
        # Swap the boards
        self.current, self.next = self.next, self.current

        # Calculate new state for every cell
        for i in range(self.sizeY):
            for ii in range(self.sizeX):
                field_sum = self.neighbours(i, ii)
                if field_sum == 3:
                    # Set cell as alive
                    self.next[i][ii] = ALIVE
                elif field_sum == 4:
                    # Retain state of cell
                    self.next[i][ii] = self.current[i][ii]
                else:
                    # Set cell as dead
                    self.next[i][ii] = DEAD

        self.iteration += 1
        if DEBUG:
            print('Iteration: ', self.iteration, '...')

    def neighbours(self, x: int, y: int) -> int:
        """Counts the number of neighbours of the cell positioned in (x,y)

        Args:
            x (int): X coordinate
            y (int): Y coordinate
        
        Returns:
            int: 
                Number of neighbours.
        """
        field = 0
        for i in range(max(0, x - 1), min(self.sizeX, x + 2)):
            for ii in range(max(0, y - 1), min(self.sizeY, y + 2)):
                field += self.current[i][ii]

        return field

    def load(self, source: str = None):
        """Load original board
        
        Args:
            source (str): File name for the source)
        """
        if source is None:
            # Generate random noise
            for i in range(self.sizeY):
                for ii in range(self.sizeX):
                    self.current[i][ii] = random.randint(DEAD, ALIVE)
                    self.next[i][ii] = self.current[i][ii]
        else:
            # Load from file
            f = open(source, "r")
            file_data = f.read()
            y = 0
            for line in file_data.split("\n"):
                x = 0
                for element in line.split(" "):
                    self.current[x][y] = int(element)
                    self.next[x][y] = self.current[x][y]
                    x += 1
                y += 1
