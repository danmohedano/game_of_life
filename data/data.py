import numpy as np
import pygame
import random
from .constants import ALIVE, DEAD, BLACK, WHITE


class Board:
    def __init__(self, size=150):
        """
        Constructor method for the board
        :param size: size of the board (default = 150)
        """
        self.size = size
        self.current = np.zeros((size, size))
        self.next = np.zeros((size, size))
        self.iteration = 1
        self.SQUARE_SIZE = 640 // size
        print("Board created for size ", self.size)

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
        for i in range(self.size):
            for ii in range(self.size):
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
        print('Iteration: ', self.iteration, '...')

    def neighbours(self, x, y):
        """
        Calculates the addition of the 9 cell field centered in (x,y)
        :param x: x coordinate
        :param y: y coordinate
        :return: sum of 9 cell field
        """
        field = 0
        for i in range(max(0, x - 1), min(self.size, x + 2)):
            for ii in range(max(0, y - 1), min(self.size, y + 2)):
                field += self.current[i][ii]

        return field

    def display(self, screen):
        """
        Displays the next board state
        :return: None
        """
        screen.fill(BLACK)
        for i in range(self.size):
            for ii in range(self.size):
                if self.next[i][ii] == ALIVE:
                    pygame.draw.rect(screen, WHITE, (ii * self.SQUARE_SIZE,
                                                     i * self.SQUARE_SIZE,
                                                     self.SQUARE_SIZE,
                                                     self.SQUARE_SIZE))

    def load(self, source=None):
        """
        Load original board
        :param source: the source
        :return:
        """
        if source is None:
            # Generate random noise
            for i in range(self.size):
                for ii in range(self.size):
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
