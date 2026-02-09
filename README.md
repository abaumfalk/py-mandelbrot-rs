# Mandelbrot calculator
Calculate a visualization of the Mandelbrot set (see https://en.wikipedia.org/wiki/Mandelbrot_set for background information).
We start from a naive implementation in pure python, implement a few optimizations and finally speed up the calculation massively using some Rust code.

This demo was inspired by a talk given at the monthly Rust Usergroup Cologne Meetup: https://rust.cologne/2026/02/04/python-speedup.html. 

## HowTo
Start the demo using uv:
uv run main.py

## Execution Time
measured on AMD Ryzen 5 3600 6-Core Processor

- v0.1 - initial Python-only version: 2,4s
- v0.2 - use pre-allocated numpy array (rather than lists): 2,6s (slower!)
- v0.3 - use lookup table for x/y coordinates: 2,7s (slightly slower!)
- v0.4 - use list comprehension: 2,4s (no difference)
- v0.5 - precalculate x/y coordinates using python lists: 2,3s (slightly faster!
