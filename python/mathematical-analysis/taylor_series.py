''' When h becomes very small, the errors start to increase due to floating-point precision.
Subtracting 2 nearly equal numbers (f(x + h) - f(x)) leads to rounding errors, which become significant for small h.
Dividing by a small h causes the overall error to increase.
'''

import numpy as np
import matplotlib.pyplot as plt

# f(x) = x^2 + x
def f(x):
    return x**2 + x

# f'(x) = 2x + 1
def f_prime(x):
    return 2 * x + 1

def forward_difference(x, h):
    return (f(x + h) - f(x)) / h

def centered_difference(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == '__main__':
    x = 1.0
    exact_derivative = f_prime(x)
    h_vals = np.logspace(-1, 1, 10)
    forward_errors = np.abs(forward_difference(x, h_vals) - exact_derivative)
    centered_errors = np.abs(centered_difference(x, h_vals) - exact_derivative)
    plt.figure(figsize=(10, 6))
    plt.loglog(h_vals, forward_errors, label='Forward difference errors', marker="o", markersize=4)
    plt.loglog(h_vals, centered_errors, label="Centered difference errors", marker="o", markersize=4)
    plt.loglog(h_vals, h_vals, label="O(h)", linestyle="--")
    plt.loglog(h_vals, h_vals ** 2, label="O(h^2)", linestyle="--")
    plt.xlabel("h")
    plt.ylabel("Error")
    plt.title("Error analysis for forward and centered differences of f(x) = x^2 + x")
    plt.legend()
    plt.grid(True)
    plt.show()