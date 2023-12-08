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
    x = np.arange(1, 6)
    print("Example 1:", add_intercept(x), file=file)

    y = np.arange(1, 10).reshape((3, 3))
    print("Example 2:", add_intercept(y), file=file)
