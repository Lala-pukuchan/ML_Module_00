import numpy as np
from prediction import simple_predict

# Input data
x = np.arange(1, 6)

# Example 1
theta1 = np.array([5, 0])
print("Example 1:", simple_predict(x, theta1))

# Example 2
theta2 = np.array([0, 1])
print("Example 2:", simple_predict(x, theta2))

# Example 3
theta3 = np.array([5, 3])
print("Example 3:", simple_predict(x, theta3))

# Example 4
theta4 = np.array([-3, 1])
print("Example 4:", simple_predict(x, theta4))
