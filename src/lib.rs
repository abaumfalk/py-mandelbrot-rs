use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod py_mandelbrot_rs {
    use pyo3::prelude::*;
    use num::Complex;

    fn mandelbrot_iterate(cx: f64, cy: f64, max_iter: u32) -> u32 {
        let c = Complex::new(cx, cy);
        let mut z = Complex::new(0.0, 0.0);
        for iteration in 0..max_iter {
            z = (z * z) + c;
            if z.norm_sqr() > 4.0 {
                return iteration;
            }
        }

        max_iter
    }

    #[pyfunction]
    fn calculate_mandelbrot(x_min: f64, x_max: f64, y_min: f64, y_max: f64, width: usize, height: usize, max_iter: u32) 
            -> Vec<Vec<u32>> {
        let x_step = (x_max - x_min) / width as f64;
        let y_step = (y_max - y_min) / height as f64;

        let mut result = vec![vec![0; width]; height];

        for y in 0..height {
            for x in 0..width {
                let cx = x_min + x as f64 * x_step;
                let cy = y_min + y as f64 * y_step;

                result[y][x] = mandelbrot_iterate(cx, cy, max_iter);
            }
        }

        result
    }
}
