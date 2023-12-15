from matrix import Matrix
from matrix import Vector

output_file = "results/ex00/result_ex00.txt"

with open(output_file, "w") as file:

    print("section.1 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    m1.shape
    print("m1.shape:\n", m1.shape, file=file)
    print("expected m1.shape:\n (3, 2)", file=file)
    print("m1.T():\n", m1.T(), file=file)
    print("expected m1.T():\n Matrix([[0., 2., 4.], [1., 3., 5.]])", file=file)
    print("m1.T().shape:\n", m1.T().shape, file=file)
    print("expected m1.T().shape:\n (2, 3)", file=file)

    print("\nsection.2 -------------------------------", file=file)
    m1 = Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])
    m1.shape
    print("m1.shape:\n", m1.shape, file=file)
    print("expected m1.shape:\n (2, 3)", file=file)
    print("m1.T():\n", m1.T(), file=file)
    print("expected m1.T():\n Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])", file=file)
    print("m1.T().shape:\n", m1.T().shape, file=file)
    print("expected m1.shape:\n (3, 2)", file=file)

    print("\nsection.3 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
    print("m1 * m2:\n", m1 * m2, file=file)
    print("expected m1 * m2:\n Matrix([[28., 34.], [56., 68.]])", file=file)

    print("\nsection.4 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print("m1 * v1:\n", m1 * v1, file=file)
    print("expected m1 * v1:\n Vector([[8], [16]])", file=file)

    print("\nsection.5 -------------------------------", file=file)
    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[2], [4], [8]])
    print("v1 + v2:\n", v1 + v2, file=file)
    print("v1 + v2:\n Vector([[3],[6],[11]])", file=file)
