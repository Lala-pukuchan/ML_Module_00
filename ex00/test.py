from matrix import Matrix
from matrix import Vector

output_file = "results/ex00/result_ex00.txt"

with open(output_file, "w") as file:

    print("section.1 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
    m1.shape
    print("m1.shape:", m1.shape, file=file)
    print("m1.T():", m1.T(), file=file)
    print("m1.T().shape:", m1.T().shape, file=file)

    print("section.2 -------------------------------", file=file)
    m1 = Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])
    m1.shape
    print("m1.shape:", m1.shape, file=file)
    print("m1.T():", m1.T(), file=file)
    print("m1.T().shape:", m1.T().shape, file=file)

    print("section.3 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
    print("m1 * m2:", m1 * m2, file=file)

    print("section.4 -------------------------------", file=file)
    m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
    v1 = Vector([[1], [2], [3]])
    print("m1 * v1:", m1 * v1, file=file)

    print("section.5 -------------------------------", file=file)
    v1 = Vector([[1], [2], [3]])
    v2 = Vector([[2], [4], [8]])
    print("v1 + v2:", v1 + v2, file=file)
