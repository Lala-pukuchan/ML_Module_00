import numpy as np


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty
    numpy.ndarray. Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if x.size == 0 or theta.size == 0 or len(theta) != 2 or x.ndim != 1:
        return None

    y_hat = theta[1] * x + theta[0]
    return y_hat


output_file = "results/ex02/result_ex02.txt"

with open(output_file, "w") as file:

    x = np.arange(1, 6)

    print("---test1---", file=file)
    theta1 = np.array([0, 0])
    print("result:\n", simple_predict(x, theta1), file=file)
    print("expected:\n", np.array([0, 0, 0, 0, 0]), file=file)

    print("---test2---", file=file)
    theta1 = np.array([1, 0])
    print("result:\n", simple_predict(x, theta1), file=file)
    print("expected:\n", np.array([1, 1, 1, 1, 1]), file=file)

    print("---test3---", file=file)
    theta1 = np.array([0, 1])
    print("result:\n", simple_predict(x, theta1), file=file)
    print("expected:\n", np.array([1, 2, 3, 4, 5]), file=file)

    print("---test4---", file=file)
    theta1 = np.array([1, 1])
    print("result:\n", simple_predict(x, theta1), file=file)
    print("expected:\n", np.array([2, 3, 4, 5, 6]), file=file)
