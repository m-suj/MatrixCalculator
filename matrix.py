import sys


class Matrix:
    def __init__(self, _m, _n=None, identity=False):
        self.m = _m
        self.n = _m if _n is None else _n
        self.matrix = [[0 for _ in range(self.n)] for __ in range(self.m)]

        identity &= self.m == self.n
        if identity:
            for i in range(_m):
                self[i][i] = 1


    """[] operator overloading"""

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value


    """Arithmetic operators overloading"""

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.m == other.m and self.n == other.n:
                m = Matrix(self.m, self.n)
                for i in range(m.m):
                    for j in range(m.n):
                        m[i][j] = self[i][j] + other[i][j]
                return m
            else:
                raise ValueError("Matrices' sizes do not match")
        else:
            raise TypeError(f"Unsupported operand type(s) for Matrix and {type(other)}")

    def __sub__(self, other):
        other *= -1
        return self + other

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            m = Matrix(self.m, self.n)
            for i in range(m.m):
                for j in range(m.n):
                    m[i][j] = self[i][j] * other
            return m
        elif isinstance(other, Matrix):
            if self.n == other.m:
                m = Matrix(self.m, other.n)
                for i in range(m.m):
                    for j in range(m.n):
                        for k in range(self.n):
                            m[i][j] += self[i][k] * other[k][j]
                return m
            else:
                raise ValueError("Matrices' sizes do not match")
        else:
            return TypeError(f"Unsupported operand type(s) for Matrix and {type(other)}")


    def __pow__(self, power: int, modulo=None):
        if self.m != self.n:
            raise ValueError("Only square matrices can be raised to a power")
        if type(power) is not int:
            raise ValueError("Exponent must be an integer")
        if power < 0:
            raise ValueError("Exponent cannot be negative")

        m = Matrix(self.m, identity=True)

        for n in range(power):
            m *= self
        return m
        # return self * self**(power-1)


    """Print matrix representation"""

    def __repr__(self):
        return '\n'.join(f"[\t{'\t'.join(map(str, row))}\t]" for row in self.matrix) + '\n'

    def print_matrix(self):
        for row in self.matrix:
            print(f"[\t{'\t'.join(map(str, row))}\t]")
        print()



class Vector(Matrix):
    def __init__(self, _m):
        super().__init__(_m, 1)


m1 = Matrix(3, 3)
print(m1)