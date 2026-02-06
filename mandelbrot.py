import time

import numpy as np
import matplotlib.pyplot as plt

from decorator import decorator
from py_mandelbrot_rs import count_iterations, mandelbrot_calc_rs

@decorator
def timeit(func, *args, **kw):
    t0 = time.time()
    result = func(*args, **kw)
    dt = time.time() - t0
    print(f"{func} took {dt} sec")
    return result


@timeit
def mandelbrot_calc(x_min, x_max, y_min, y_max, width, height, max_iter):
    """ Calculate mandelbrot image.

    :param x_min: minimum x-coordinate
    :param x_max: maximum x-coordinate
    :param y_min: minimum y-coordinate
    :param y_max: maximum y-coordinate
    :param width: width of image
    :param height: height of image
    :param max_iter: iteration limit
    """
    return mandelbrot_calc_rs(x_min, x_max, y_min, y_max, width, height, max_iter)


def show(data):
    """ plot and display precalculated data

    :param data: data to be plotted
    """
    plt.imshow(data, cmap="hot")
    plt.show()


if __name__ == "__main__":
    mandelbrot = mandelbrot_calc(-2, 1, -1.5, 1.5, 1000, 1000, 120)
    show(mandelbrot)

