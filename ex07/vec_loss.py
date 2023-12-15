import numpy as np


def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array,
    without any for loop. The two arrays must have the same dimensions.
    Args:
        y: has to be an numpy.array, a vector.
        y_hat: has to be an numpy.array, a vector.
        Returns:
        The half mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.array.
        None if y and y_hat does not share the same dimensions.
        Raises:
        This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    if y.shape != y_hat.shape:
        return None

    # vectorized loss function
    m = len(y)
    loss = np.dot((y_hat - y).T, (y_hat - y)) / (2 * m)
    return loss.item()

output_file = "results/ex07/result_ex07.txt"

with open(output_file, "w") as file:
    print("---test.1---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [2], [3], [4]])
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 0", file=file)

    print("\n---test.2---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 3.75", file=file)

    print("\n---test.3---", file=file)
    y_hat = np.array([[1], [2], [4], [8]])
    y = np.array([[1], [1], [1], [1]])
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 7.375", file=file)
