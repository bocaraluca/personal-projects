import numpy as np
from math import sqrt, pi

# f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Trapezium rule
def trapezium_rule(func, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = func(x)
    h = (b - a) / n
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

if __name__ == '__main__':
    n = 1000
    a_vals = [1, 5, 10, 20, 50, 100]
    results = []
    for a in a_vals:
        integral = trapezium_rule(f, -a, a, n)
        results.append(integral)
    for a, result in zip(a_vals, results):
        print(f'a = {a} => integral ≈ {result:.6f}')
    print(f'sqrt(pi): {sqrt(pi):.6f}')