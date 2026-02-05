import numpy as np
import matplotlib.pyplot as plt


def count_iterations(c, max_iter):
    """ Counts the number of iterations until the function diverges or max_iter is reached.

    :param c: coordinate
    :param max_iter: interation limit
    :return: number of iterations
    """
    z = complex(0, 0)
    for iteration in range(max_iter):
        z = (z*z) + c
        if abs(z) > 2:
            return iteration

    return max_iter


def mandelbrot(max_iter, number):
    """ Draw mandelbrot image.

    :param max_iter: iteration limit
    :param number: number of samples
    """
    # location and size of the atlas rectangle
    real_axis = np.linspace(-0.22, -0.219, number)
    imaginary_axis = np.linspace(-0.70, -0.699, number)
    real_axis_len = len(real_axis)
    imaginary_axis_len = len(imaginary_axis)

    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((real_axis_len, imaginary_axis_len))

    # color each point in the atlas depending on the iteration count
    for ix in range(real_axis_len):
        for iy in range(imaginary_axis_len):
            cx = real_axis[ix]
            cy = imaginary_axis[iy]
            c = complex(cx, cy)

            atlas[ix, iy] = count_iterations(c, max_iter)

    # plot and display mandelbrot set
    plt.imshow(atlas.T, interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    mandelbrot(120, 1000)
