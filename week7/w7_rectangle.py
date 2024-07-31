from w7_shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.shape_type = 'Rectangle'
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    # override area method
    def area(self):
        return self.__width * self.__height

    # override __str__ method
    def __str__(self):
        shape_info = super().__str__()
        rectangle_info = f', width: {self.__width}, height: {self.__height}'
        return shape_info + rectangle_info

if __name__ == '__main__':
    r = Rectangle('ABCD', 10, 5)
    print(r)