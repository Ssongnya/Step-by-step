class Circle :
    def __init__(self, radius):
        self.circum = radius**2 * 3.14
        print(f'원의 면적: {self.circum :.2f}')

Circle(2)