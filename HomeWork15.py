import math
class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        if not isinstance(width, int or float) and not isinstance(height, int or float):
            raise ValueError('width and height must be only int or float')
        self.width = width
        self.height = height

    def volume(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()
    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.volume() + other.volume()
        if isinstance(other, int | float):
            return self.volume() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.volume()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.volume() * other
        return NotImplemented

    # def __rmul__(self, other):
    #     return other * self.volume()

    def __str__(self):
        return f'Width - {self.width}, Height - {self.height}.'


fist_rectangle = Rectangle(3, 3)
second_rectangle = Rectangle(4, 4)
n = 17
x = Rectangle(2, 2)
print(x + 2)
print(fist_rectangle + second_rectangle)
print(fist_rectangle * n)



class Rational:

    def __init__(self, a: int, b: int):
        if not isinstance(a and b, int):
            raise TypeError('Only int')
        if not self.b:
            raise ZeroDivisionError("Can't be zero")
        self.a = a
        self.b = b



    def __gt__(self, other): # більше
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):# менше
        return self.a / self.b < other.a / other.b


    def __eq__(self, other):
        grst_cm_dvr = math.gcd(self.a, self.b)
        self.a //= grst_cm_dvr
        self.b //= grst_cm_dvr

        grst_cm_dvr = math.gcd(other.a, other.b)
        other.a //= grst_cm_dvr
        other.b //= grst_cm_dvr
        return (self.a, self.b) == (other.a, other.b)

    def __ne__(self, other):
        return not self.__eq__(other)


    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        b = self.b * other.b
        a = b // self.b * self.a - b // other.b * other.a
        return Rational(a, b)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        b = self.b * other.b
        a = b // self.b * self.a - b // other.b * other.a
        return Rational(b, a)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        res = 1 if self.a * self.b > 0 else - 1
        b = abs(self.b) * abs(other.b)
        a = b // abs(self.b) * abs(self.a) - b // abs(other.b) * abs(other.a)
        self.a = res * a
        self.b = b
        return self

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = (self.a * other.b + other.a * self.b)
        b = (self.b * other.b)
        return Rational(a, b)

    def __radd__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = (self.a * other.b + other.a * self.b)
        b = (self.b * other.b)
        return Rational(a, b)

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        a = (self.a * other.b + other.a * self.b)
        b = (self.b * other.b)
        return Rational(a, b)

    def __str__(self):
        res = '' if self.a * self.b >= 0 else '-'
        a, b = abs(self.a), abs(self.b)
        grst_cm_dvr = math.gcd(a, b)
        a //= grst_cm_dvr
        b //= grst_cm_dvr
        if a == b:
            return f'{res}1'
        if b == 1:
            return f'{res}{a}'
        if b < a:
            return f'{res}{a // b} {a - a // b * b} / {b}'
        return f'{res}{a} / {b}'



example_1 = Rational(1, 4)
example_2 = Rational(3, 6)
print(example_1 + 4 - example_2)
print(example_1 > example_2)
print(example_2 < example_1)
print(example_1 - 4 - example_2)
print(example_1 != example_2)
print(example_2 == example_1)
