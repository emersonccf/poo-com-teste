from math import hypot


class AddTypeDifferentError(Exception):
    pass


class MultiplyTypeDifferentError(Exception):
    pass


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # return f'Vector({self.x}, {self.y})' # new format
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        if type(other) is not Vector:
            raise AddTypeDifferentError('Erro ao tentar somar: '
                                        '%r com %r' % (self, other))
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if type(scalar) is not int:
            raise MultiplyTypeDifferentError(
                'Tentativa de multiplicar por não inteiro')
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if type(other) is not Vector:
            return False
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # faster than bool(abs(self))
        return bool(self.x or self.y)
