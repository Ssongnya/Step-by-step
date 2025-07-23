class Rectangle:
    def __init__(self, width, length):
        self.extent = width * length
        print(f'사각형의 면적: {self.extent}')

Rectangle(4, 5)