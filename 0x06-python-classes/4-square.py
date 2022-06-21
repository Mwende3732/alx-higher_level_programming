#!/usr/bin/python3
"""class Square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """square initialization"""
        self.size = size

    @property
    def size(self):
        """returns current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """validates v     raise TypeError("size must be an integer")
  alue"""
        if type(value) is not int:
             elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of square"""
        return (self.__size * self.__size)
