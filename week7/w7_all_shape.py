from w7_circle import Circle
from w7_rectangle import Rectangle
from w7_square import Square

if __name__ == '__main__':
    c = Circle('O1', 10)
    r = Rectangle('ABCD', 10, 5)
    s = Square('ABCD', 5)

    shapes = [c, r, s]

    for s in shapes:
        print(s)

    max_area = 0
    for s in shapes:
        if s.area() > max_area:
            max_area = s.area()
            max_shape = s
    
    print(f'Shape with the largest area: {max_shape}')