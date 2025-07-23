class Shape:
    def area(self) :
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self) :
        extent = self.length ** 2
        return extent

result = Square(3)
print("정사각형의 면적:", result.area())