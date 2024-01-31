from matrix import Matrix

m1 = Matrix(3, 2, matrix=[
    [1, 2], [3, 4], [5, 6]
])
m2 = Matrix(2, 4, matrix=[
    [2, 1, 3, 7], [6, 9, 6, 9]
])

print(m1*m2)
#print(m2*m1)