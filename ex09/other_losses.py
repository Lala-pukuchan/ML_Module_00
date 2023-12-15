import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt


def mse_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    return np.mean((y - y_hat) ** 2)


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
    return np.mean(np.abs(y - y_hat))


def r2score_(y, y_hat):
    if (
        not (isinstance(y, np.ndarray) and isinstance(y_hat, np.ndarray))
        or y.shape != y_hat.shape
    ):
        return None
    numerator = ((y_hat - y) ** 2).sum()
    denominator = ((y - y.mean()) ** 2).sum()
    if denominator == 0:
        return -5
    return 1 - numerator / denominator


output_file = "results/ex09/result_ex09.txt"

with open(output_file, "w") as file:
    print("--- MSE ---", file=file)

    print("--- ex.01 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [2], [3], [4]])
    print("result:\n", mse_(y, y_hat), file=file)
    print("expected:\n 0", file=file)

    print("--- ex.02 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("result:\n", mse_(y, y_hat), file=file)
    print("expected:\n 7.5", file=file)

    print("--- ex.03 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [4], [8], [16]])
    print("result:\n", mse_(y, y_hat), file=file)
    print("expected:\n", mean_squared_error(y, y_hat), file=file)

    print("\n--- RMSE ---", file=file)

    print("--- ex.01 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("result:\n", rmse_(y, y_hat), file=file)
    print("expected:\n 2.738...", file=file)

    print("--- ex.02 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [4], [8], [16]])
    print("result:\n", rmse_(y, y_hat), file=file)
    print("expected:\n", sqrt(mean_squared_error(y, y_hat)), file=file)

    print("\n--- MAE ---", file=file)

    print("--- ex.01 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [2], [3], [4]])
    print("result:\n", mae_(y, y_hat), file=file)
    print("expected:\n 0", file=file)

    print("--- ex.02 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("result:\n", mae_(y, y_hat), file=file)
    print("expected:\n 2.5", file=file)

    print("--- ex.03 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [4], [8], [16]])
    print("result:\n", mae_(y, y_hat), file=file)
    print("expected:\n", mean_absolute_error(y, y_hat), file=file)

    print("\n--- R2score ---", file=file)

    print("--- ex.01 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[0], [0], [0], [0]])
    print("result:\n", r2score_(y, y_hat), file=file)
    print("expected:\n -5", file=file)
    
    print("--- ex.02 ---", file=file)
    y_hat = np.array([[1], [2], [3], [4]])
    y = np.array([[1], [4], [8], [16]])
    print("result:\n", r2score_(y, y_hat), file=file)
    print("expected:\n", r2_score(y, y_hat), file=file)
