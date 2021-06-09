import threading
import numpy as np
import pygame
import random
from .constants import ALIVE, DEAD
from config import DEBUG


class Board:
    def __init__(self, size_x: int, size_y: int):
        """
        Constructor method for the board
        :param size_x: width of the board
        :param size_y: height of the board
        """
        self.sizeX = size_x
        self.sizeY = size_y
        self.current = np.zeros((size_x, size_y))
        self.next = np.zeros((size_x, size_y))
        self.iteration = 0

        if DEBUG:
            print("Initialized board [size=({},{})] ".format(self.sizeX, self.sizeY))

    def iterate(self):
        """
        Calculates an iteration for the board:
        1. Swaps the boards
        2. Calculates new state in 'next' board
        :return: None
        """
        # Swap the boards
        self.current, self.next = self.next, self.current

        # Calculate new state for every cell
        for i in range(self.sizeX):
            for ii in range(self.sizeY):
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

    def neighbours(self, x, y):
        """
        Calculates the addition of the 9 cell field centered in (x,y)
        :param x: x coordinate
        :param y: y coordinate
        :return: sum of 9 cell field
        """
        field = 0
        for i in range(max(0, x - 1), min(self.sizeX, x + 2)):
            for ii in range(max(0, y - 1), min(self.sizeY, y + 2)):
                field += self.current[i][ii]

        return field

    def load(self, source=None):
        """
        Load original board
        :param source: the source
        :return:
        """
        if source is None:
            # Generate random noise
            for i in range(self.sizeX):
                for ii in range(self.sizeY):
                    self.current[i][ii] = random.randint(DEAD, ALIVE)
                    self.next[i][ii] = self.current[i][ii]
        else:
            # Load from file
            f = open(source, "r")
            file_data = f.read()
            x = 0
            for line in file_data.split("\n"):
                y = 0
                for element in line.split(" "):
                    self.current[x][y] = int(element)
                    self.next[x][y] = self.current[x][y]
                    y += 1
                x += 1
