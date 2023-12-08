import numpy as np
import matplotlib.pyplot as plt


def predict_(x, theta):
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    return theta[0] + theta[1] * x


def plot_with_loss(x, y, theta, output_file):
    if not (
        isinstance(x, np.ndarray)
        and isinstance(y, np.ndarray)
        and isinstance(theta, np.ndarray)
    ):
        return
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return
    if x.ndim != 1 or y.ndim != 1 or len(theta) != 2:
        return

    # Reshape theta to be a (2, 1) array
    theta = theta.reshape(2, 1)

    y_hat = predict_(x, theta)

    plt.scatter(x, y, color="blue", label="Data points")
    plt.plot(x, y_hat, color="red", label="Prediction line")

    for xi, yi, y_hat_i in zip(x, y, y_hat.ravel()):
        plt.plot([xi, xi], [yi, y_hat_i], color="green", linestyle="dotted")

    plt.title("Prediction, Data, and Loss")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig(output_file)
    plt.close()


output_file_1 = "results/ex08/result_ex08_figure1"
output_file_2 = "results/ex08/result_ex08_figure2"
output_file_3 = "results/ex08/result_ex08_figure3"

x = np.arange(1, 6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
theta1 = np.array([18, -1])
plot_with_loss(x, y, theta1, output_file_1)

theta2 = np.array([14, 0])
plot_with_loss(x, y, theta2, output_file_2)

theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3, output_file_3)
