import argparse
import time
import timeit
from matplotlib import pyplot


def mandelbrot_iterate(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter


def calculate_mandelbrot(x_min, x_max, y_min, y_max, width, height, iterations):
    x_step = (x_max - x_min) / width
    y_step = (y_max - y_min) / height

    result = []
    for y in range(height):
        row = []
        for x in range(width):
            c = complex(x_min + x * x_step, y_min + y * y_step)
            row.append(mandelbrot_iterate(c, iterations))
        result.append(row)

    return result

def show(data):
    pyplot.imshow(data, cmap="hot")
    pyplot.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--iterations", type=int, help="Number of iterations", default=100)
    parser.add_argument("--range", type=float, nargs=4, default=[-2, 1, -1.5, 1.5],
                        help="xmin, xmax, ymin, ymax")
    parser.add_argument("--width", type=int, help="Width of image", default=1000)
    parser.add_argument("--height", type=int, help="Height of image", default=1000)
    parser.add_argument("--timeit", help="Measure execution time rather than displaying the image", action="store_true")
    args = parser.parse_args()

    def run():
        return calculate_mandelbrot(args.range[0], args.range[1], args.range[2], args.range[3],
                                   args.width, args.height, args.iterations)

    if args.timeit:
        times = 10
        print(f"running {times} times...")
        t = timeit.Timer(run, timer=time.process_time)
        time = t.timeit(times)
        print(f"took {time/times} seconds per run")
    else:
        mandelbrot = run()
        show(mandelbrot)