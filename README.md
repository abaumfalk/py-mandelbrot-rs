# Mandelbrot calculator
Calculate a visualization of the Mandelbrot set (see https://en.wikipedia.org/wiki/Mandelbrot_set for background information).
We start from a naive implementation in pure python, implement a few optimizations and finally speed up the calculation massively using some Rust code.

This demo was inspired by a talk given at the monthly Rust Usergroup Cologne Meetup: https://rust.cologne/2026/02/04/python-speedup.html. 

## HowTo
Start the demo using uv:
uv run main.py
