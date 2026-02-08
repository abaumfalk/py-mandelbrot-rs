import argparse


def calculate_mandelbrot(x_min, x_max, y_min, y_max, width, height, iterations):
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--iterations", type=int, help="Number of iterations", default=100)
    parser.add_argument("--range", type=float, nargs=4, default=[-2, 1, -1.5, 1.5],
                        help="xmin, xmax, ymin, ymax")
    parser.add_argument("--width", type=int, help="Width of image", default=1000)
    parser.add_argument("--height", type=int, help="Height of image", default=1000)
    args = parser.parse_args()

    set = calculate_mandelbrot(args.range[0], args.range[1], args.range[2], args.range[3],
                               args.width, args.height, args.iterations)
