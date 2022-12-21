#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

     # Property
     @property
     def size(self):
         return self.__size

     # Setter modifies
     @size.setter
     def size(self, value):
         if type(value) != int:
             raise TypeError('size must be an integer')
         elif value < 0:
             raise ValueError('size must be >= 0')
         else:
             self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        size = self.__size

        if size == 0:
            print()

        for row in range(size):
            print('#' * size)
