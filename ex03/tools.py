import numpy as np


def add_intercept(x):
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None

    m = x.shape[0]
    intercept = np.ones((m, 1))

    # Reshape x to a 2D array if it's 1D
    if x.ndim == 1:
        x = x.reshape(m, 1)

    return np.hstack((intercept, x))


output_file = "results/ex03/result_ex03.txt"

with open(output_file, "w") as file:
    print("---test.1---", file=file)
    x = np.arange(1, 6)
    print("before add_intercept:\n", x, file=file)
    print("afer add_intercept:\n", add_intercept(x), file=file)

    print("\n---test.2---", file=file)
    y = np.arange(1, 10).reshape((3, 3))
    print("before add_intercept:\n", y, file=file)
    print("afer add_intercept:\n", add_intercept(y), file=file)
