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
    # location and size of the atlas rectangle
    real_axis = np.linspace(x_min, x_max, width)
    imaginary_axis = np.linspace(y_min, y_max, height)

    # 2-D array to represent mandelbrot atlas
    atlas = np.empty((height, width))

    # color each point in the atlas depending on the iteration count
    for ix in range(height):
        for iy in range(width):
            cx = real_axis[ix]
            cy = imaginary_axis[iy]
            c = complex(cx, cy)

            atlas[ix, iy] = count_iterations(c, max_iter)

    return atlas


def show(data):
    """ plot and display precalculated data

    :param data: data to be plotted
    """
    plt.imshow(data.T, cmap="hot")
    plt.show()


if __name__ == "__main__":
    mandelbrot = mandelbrot_calc(-0.22, -0.219, -0.70, -0.699, 1000, 1000, 120)
    show(mandelbrot)
