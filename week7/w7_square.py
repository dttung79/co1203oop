from w7_rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self.shape_type = 'Square'
    
    @property
    def side(self):
        return self.width
    
    @side.setter
    def side(self, side):
        self.width = side
        self.height = side

if __name__ == '__main__':
    s = Square('ABCD', 5)
    print(s)
    # change side
    s.side = 10
    print(s)