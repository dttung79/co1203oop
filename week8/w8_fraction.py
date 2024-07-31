class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        self.a = a
        self.b = b
    
    def show(self):
        if self.a == 0:
            print(0, end='')
        elif self.a * self.b > 0:
            print(f"{abs(self.a)}/{abs(self.b)}", end='')
        else:
            print(f"-{abs(self.a)}/{abs(self.b)}", end='')