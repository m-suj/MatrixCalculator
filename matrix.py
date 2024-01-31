class Matrix:
    def __init__(self, _m, _n=None, identity=False, matrix=None):
        self.m = _m
        self.n = _m if _n is None else _n
        if matrix:
            self.matrix = matrix
        else:
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


    """Column/Row getters"""

    def get_row(self, i):
        return self[i]

    def get_column(self, j):
        return [self.matrix[i][j] for i in range(self.m)]


    """Arithmetic operations"""

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
        """Defining multiplication operations that include matrices"""
        # Matrix * Scalar
        if isinstance(other, float) or isinstance(other, int):
            return Matrix(self.m, self.n, matrix=[[self[i][j] * other for j in range(self.n)] for i in range(self.m)])

        # Matrix * Matrix
        elif isinstance(other, Matrix):
            if self.n == other.m:  # Multiplication condition
                return Matrix(self.m, other.n, matrix=[[sum([self[i][k] * other[k][j] for k in range(self.n)]) for j in range(other.n)] for i in range(self.m)])
            else:
                raise ValueError("Matrices' sizes do not match")
        else:
            return TypeError(f"Unsupported operand type(s) for Matrix and {type(other)}")

    def __rmul__(self, other):
        """Scalar * Matrix -> Matrix * Scalar"""
        return self * other

    def __pow__(self, power: int, modulo=None):
        """Defining 'Matrix^c' for c∈Z"""
        if self.m != self.n:
            raise ValueError("Only square matrices can be raised to a power")
        if type(power) is not int:
            raise ValueError("Exponent must be an integer")
        if power < 0:
            # n∈N: Matrix^(-n) = (Matrix^(-1))^n
            return self.inverse() ** (-power)

        m = Matrix(self.m, identity=True)
        for n in range(power):
            m *= self
        return m


    """Advanced matrix operations"""

    def transpose(self):
        m = Matrix(self.n, self.m)
        for i in range(self.m):
            for j in range(self.n):
                m[j][i] = self[i][j]
        return m

    def minor(self, i, j):
        m_tab = [[] for _ in range(self.m - 1)]
        m_i = 0

        for _i in range(self.m):
            for _j in range(self.n):
                if _i != i and _j != j:
                    m_tab[m_i].append(self[_i][_j])
            if _i == i:
                continue
            m_i += 1

        m = Matrix(self.m - 1)
        m.matrix = m_tab
        return m.determinant()

    def cofactor(self):
        m = Matrix(self.m)
        # m.matrix = [[(-1)**(i + j) * self.minor(j, i) for j in range(self.m)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                m[i][j] = (-1)**(i + j) * self.minor(j, i)
        return m


    def inverse(self):
        if self.determinant() == 0:
            raise ValueError("Linear dependent matrix is not invertible")

        return (1 / self.determinant()) * self.cofactor()


    """Algebraic row operations"""
    def concatenate(self, other):
        raise NotImplemented
        # TODO: implement matrices concatenation

    def row_reduction(self, transform_matrix):
        raise NotImplemented
        # TODO: row reduction, thinking about the expected results and usage of Gauss elimination tool
        #       to figure out implementations of row reduction operations



    """Determinant"""
    def determinant(self):
        if self.m != self.n:
            raise ValueError("Matrix must be square to take the determinant")
        if self.m == 1:
            return self[0][0]
        else:
            det = 0
            i = 0

            for j in range(self.n):
                det += (-1)**(i+j) * self[i][j] * self.minor(i, j)
            return det


    # TODO: Eigen algebra


    """Print matrix representation"""
    def __repr__(self):
        return '\n'.join(f"[\t{'\t'.join(map(str, [round(x, 3) for x in row]))}\t]" for row in self.matrix) + '\n'

    def print_matrix(self):
        for row in self.matrix:
            print(f"[\t{'\t'.join(map(str, row))}\t]")
        print()



class Vector(Matrix):
    def __init__(self, _m):
        super().__init__(_m, 1)

