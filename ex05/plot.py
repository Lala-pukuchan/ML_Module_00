import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend for matplotlib
# matplotlib.use("Agg")


def plot(x, y, theta, output_file):
    """
    Plot the data and prediction line from three non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of dimension m * 1.
        y: has to be an numpy.array, a vector of dimension m * 1.
        theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exceptions.
    """

    # return if x, y, theta aren't array
    if not (
        isinstance(x, np.ndarray)
        and isinstance(y, np.ndarray)
        and isinstance(theta, np.ndarray)
    ):
        return
    
    # return if x, y, theta aren't array
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return
    
    # reshape if x, y, theta are array
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    if y.ndim == 1:
        y = y.reshape(-1, 1)
    if theta.ndim == 1:
        theta = theta.reshape(-1, 1)

    # check shape
    if theta.shape != (2, 1) or x.shape[1] != 1 or y.shape[1] != 1 or x.shape[0] != y.shape[0]:
        return

    # Compute the prediction
    y_hat = theta[0] + theta[1] * x

    plt.scatter(x, y, color="blue", label="Data points")
    plt.plot(x, y_hat, color="red", label="Prediction line")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data and Prediction Line")
    plt.legend()

    # Save the plot to a file
    plt.savefig(output_file)
    plt.close()


output_file_1 = "results/ex05/result_ex05_figure1"
output_file_2 = "results/ex05/result_ex05_figure2"
output_file_3 = "results/ex05/result_ex05_figure3"

plot(np.array([0, 1]), np.array([0, 1]), np.array([0, 1]), output_file_1)
plot(np.array([0, 1]), np.array([0, 1]), np.array([1, 1]), output_file_2)
plot(np.array([0, 2]), np.array([0, 0]), np.array([-1, 1]), output_file_3)
