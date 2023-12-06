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
