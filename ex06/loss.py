import numpy as np


def loss_elem_(y, y_hat):
    """
      Description:
              Calculates all the elements (y_pred - y)^2
              of the loss function.
      Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
      Returns:
              J_elem: numpy.array, a vector of dimension
              (number of the training examples,1).
              None if there is a dimension matching problem
              between X, Y or theta.
              None if any argument is not of the expected type.
      Raises:
              This function should not raise any Exception.
    """
    if not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray)):
        return None
    if y.shape != y_hat.shape:
        return None

    return ((y_hat - y) ** 2) / (2 * len(y))


def loss_(y, y_hat):
    """
      Description:
              Calculates the value of loss function.
      Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
      Returns:
              J_value : has to be a float.
              None if there is a dimension matching problem
              between X, Y or theta.
              None if any argument is not of the expected type.
      Raises:
              This function should not raise any Exception.
    """
    if not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray)):
        return None
    if y.shape != y_hat.shape:
        return None

    return np.sum(loss_elem_(y, y_hat))


def predict_(x, theta):
    # Ensure x is a 2D array
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    # Compute the prediction
    y_hat = theta[0] + theta[1] * x
    return y_hat


output_file = "results/ex06/result_ex06.txt"

with open(output_file, "w") as file:
    print("---test.1---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [2], [3], [4]])
    print("Loss Elements:\n", loss_elem_(y, y_hat), file=file)
    print("expected Loss Elements:\n", np.array([[0], [0], [0], [0]]), file=file)
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 0", file=file)

    print("\n---test.2---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("Loss Elements:\n", loss_elem_(y, y_hat), file=file)
    print(
        "expected Loss Elements:\n", np.array([[0.125], [0.5], [1.125], [2]]), file=file
    )
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 3.75", file=file)

    print("\n---test.3---", file=file)
    y_hat = np.array([[1], [2], [4], [8]])
    y = np.array([[1], [1], [1], [1]])
    print("Loss Elements:\n", loss_elem_(y, y_hat), file=file)
    print(
        "expected Loss Elements:\n",
        np.array([[0], [0.125], [1.125], [6.125]]),
        file=file,
    )
    print("Loss:\n", loss_(y, y_hat), file=file)
    print("expected Loss:\n 7.375", file=file)
