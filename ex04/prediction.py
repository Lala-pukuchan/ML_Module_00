import numpy as np


def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """

    # x and theta should be array
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None

    # x and theta shouldn't be empty
    if x.size == 0 or theta.size == 0:
        return None

    # reshape x if it's column vector
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    # reshape theta if it's array
    if theta.ndim != 2:
        theta = theta.reshape(-1, 1)

    # theta should be 2*1 and x should be m*1
    if theta.shape != (2, 1) or x.shape[1] != 1:
        return None

    # insert 1 to x's first column
    x_insert = np.hstack((np.ones((x.shape[0], 1)), x))

    # Compute the prediction
    y_hat = np.dot(x_insert, theta)
    return y_hat.ravel()


output_file = "results/ex04/result_ex04.txt"

with open(output_file, "w") as file:
    x = np.arange(1, 6)

    print("---test1---", file=file)
    theta1 = np.array([0, 0])
    print("result:\n", predict_(x, theta1), file=file)
    print("expected:\n", np.array([0, 0, 0, 0, 0]), file=file)

    print("---test2---", file=file)
    theta1 = np.array([1, 0])
    print("result:\n", predict_(x, theta1), file=file)
    print("expected:\n", np.array([1, 1, 1, 1, 1]), file=file)

    print("---test3---", file=file)
    theta1 = np.array([0, 1])
    print("result:\n", predict_(x, theta1), file=file)
    print("expected:\n", np.array([1, 2, 3, 4, 5]), file=file)

    print("---test4---", file=file)
    theta1 = np.array([1, 1])
    print("result:\n", predict_(x, theta1), file=file)
    print("expected:\n", np.array([2, 3, 4, 5, 6]), file=file)
