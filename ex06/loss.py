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

    return (y_hat - y) ** 2


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

    return np.mean((y_hat - y) ** 2) / 2


def predict_(x, theta):
    # Ensure x is a 2D array
    if x.ndim == 1:
        x = x.reshape(-1, 1)

    # Compute the prediction
    y_hat = theta[0] + theta[1] * x
    return y_hat


output_file = "results/ex06/result_ex06.txt"

with open(output_file, "w") as file:

    x1 = np.array([[0.0], [1.0], [2.0], [3.0], [4.0]])
    theta1 = np.array([[2.0], [4.0]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.0], [7.0], [12.0], [17.0], [22.0]])
    print("Example 1 Loss Elements:", loss_elem_(y1, y_hat1), file=file)
    print("Example 1 Loss:", loss_(y1, y_hat1), file=file)

    x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
    theta2 = np.array([[0.0], [1.0]])
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
    print("Example 2 Loss:", loss_(y2, y_hat2), file=file)
    print("Example 3 Loss:", loss_(y2, y2), file=file)
