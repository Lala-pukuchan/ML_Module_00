import numpy as np
import matplotlib.pyplot as plt


def predict_(x, theta):
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    return theta[0] + theta[1] * x


def loss_(y, y_hat):
    return 0.5 * np.mean((y_hat - y) ** 2)


def plot_with_loss(x, y, theta):
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
    loss = loss_(y, y_hat)

    plt.scatter(x, y, color="blue", label="Data points")
    plt.plot(x, y_hat, color="red", label="Prediction line")

    for xi, yi, y_hat_i in zip(x, y, y_hat.ravel()):
        plt.plot([xi, xi], [yi, y_hat_i], color="green", linestyle="dotted")

    plt.title(f"Prediction, Data, and Loss (J = {loss:.2f})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("plot_with_loss.png")
    plt.close()


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 8, 11, 14, 17])

theta2 = np.array([14, 0])
plot_with_loss(x, y, theta2)
