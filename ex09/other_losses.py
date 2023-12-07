import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt


def mse_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    return np.mean((y_hat - y) ** 2)


def rmse_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    return np.sqrt(mse_(y, y_hat))


def mae_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    return np.mean(np.abs(y_hat - y))


def r2score_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    u = ((y - y_hat) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - u / v


# x = np.array([0, 15, -9, 7, 12, 3, -21])
# y = np.array([2, 14, -13, 5, 12, 4, -19])
# print("--- MSE ---")
# print(mse_(x,y))
# print(mean_squared_error(x,y))
# print("--- RMSE ---")
# print(rmse_(x,y))
# print(sqrt(mean_squared_error(x,y)))
# print("--- MAE ---")
# print(mae_(x,y))
# print(mean_absolute_error(x,y))
# print("--- R2 ---")
# print(r2score_(x,y))
# print(r2_score(x,y))
