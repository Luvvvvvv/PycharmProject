from time import sleep
from numpy import dot
from numpy.linalg import inv
from numpy import mat


def least_squares(x, y):
    theta = dot(dot(inv(dot(x.T, x)), x.T), y)
    return theta


if __name__ == "__main__":
    x = mat([[5.72, 6.22, 5.49], [6.00, 6.65, 6.09],
             [6.50, 6.83, 6.52], [6.14, 6.75, 6.86],
             [6.43, 6.81, 6.58], [6.52, 6.87, 6.73],
             [6.86, 7.46, 6.93], [6.64, 7.05, 7.15],
             [6.19, 6.24, 6.13], [6.28, 6.15, 6.30],
             [6.41, 6.57, 6.26], [6.26, 6.65, 6.43]])
    y = mat([[6.52], [6.68], [7.05], [7.21], [6.94],
             [7.34], [7.61], [8.17], [6.62], [6.95], [6.92], [7.18]])
    print(least_squares(x, y))

sleep(5)
