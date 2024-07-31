from w7_shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.shape_type = 'Circle'
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    
    def area(self):
        return 3.14159 * self.__radius ** 2

    def __str__(self):
        shape_info = super().__str__()
        circle_info = f', radius: {self.__radius}'
        return shape_info + circle_info

if __name__ == '__main__':
    c = Circle('O1', 10)
    print(c)