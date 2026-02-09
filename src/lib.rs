use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod py_mandelbrot_rs {
    use pyo3::prelude::*;
    use num::Complex;

    #[pyfunction]
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
}
