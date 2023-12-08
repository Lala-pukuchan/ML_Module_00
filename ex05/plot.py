import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend for matplotlib
matplotlib.use("Agg")


def plot(x, y, theta, output_file):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if not (
        isinstance(x, np.ndarray)
        and isinstance(y, np.ndarray)
        and isinstance(theta, np.ndarray)
    ):
        return
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return
    if theta.shape != (2, 1) or x.ndim != 1:
        return

    # Reshape x to a 2D array if it's 1D
    if x.ndim == 1:
        x = x.reshape(-1, 1)

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

x = np.arange(1, 6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
theta1 = np.array([[4.5], [-0.2]])
plot(x, y, theta1, output_file_1)

theta2 = np.array([[-1.5], [2]])
plot(x, y, theta2, output_file_2)

theta3 = np.array([[3], [0.3]])
plot(x, y, theta3, output_file_3)
