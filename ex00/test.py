from matrix import Matrix
from matrix import Vector

print("section.1 -------------------------------")
m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])

m1.shape
print("m1.shape:", m1.shape)

# transpose
print("m1.T():", m1.T())
print("m1.T().shape:", m1.T().shape)


print("section.2 -------------------------------")
m1 = Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])

m1.shape
print("m1.shape:", m1.shape)
# transpose
print("m1.T():", m1.T())
print("m1.T().shape:", m1.T().shape)


print("section.3 -------------------------------")
m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])

m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])

print("m1 * m2:", m1 * m2)


print("section.4 -------------------------------")
m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])

v1 = Vector([[1], [2], [3]])

print("m1 * v1:", m1 * v1)


print("section.5 -------------------------------")
v1 = Vector([[1], [2], [3]])
v2 = Vector([[2], [4], [8]])

print("v1 + v2:", v1 + v2)
