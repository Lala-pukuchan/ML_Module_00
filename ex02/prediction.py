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


# x = np.arange(1, 6)

# theta1 = np.array([5, 0])
# print("Example 1:", simple_predict(x, theta1))

# theta2 = np.array([0, 1])
# print("Example 2:", simple_predict(x, theta2))

# theta3 = np.array([5, 3])
# print("Example 3:", simple_predict(x, theta3))

# theta4 = np.array([-3, 1])
# print("Example 4:", simple_predict(x, theta4))
