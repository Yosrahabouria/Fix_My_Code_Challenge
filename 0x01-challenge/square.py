#!/usr/bin/python3

class square():
    width = 0
    height = 0

    def __init__(self, width=0):
        self.width = width
        self.height = width

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter of square"""
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12)  # Since height is automatically set to width
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
