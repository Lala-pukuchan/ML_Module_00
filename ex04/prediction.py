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

    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    if theta.shape != (2, 1) or x.ndim != 1:
        return None

    # -1 is a placeholder for the number of rows when not known
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    # Compute the prediction
    y_hat = theta[0] + theta[1] * x
    return y_hat


# x = np.arange(1, 6)

# theta1 = np.array([[5], [0]])
# print("Example 1:", predict_(x, theta1))

# theta2 = np.array([[0], [1]])
# print("Example 2:", predict_(x, theta2))

# theta3 = np.array([[5], [3]])
# print("Example 3:", predict_(x, theta3))

# theta4 = np.array([[-3], [1]])
# print("Example 4:", predict_(x, theta4))
