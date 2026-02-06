use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod py_mandelbrot_rs {
    use pyo3::prelude::*;
    use num::Complex;

    #[pyfunction]
    fn count_iterations(cx: f64, cy: f64, max_iter: u32) -> u32 {
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
    fn mandelbrot_calc_rs(x_min: f64, x_max: f64, y_min: f64, y_max: f64, width: usize, height: usize, max_iter: u32) 
            -> Vec<Vec<u32>> {
        let real_axis: Vec<f64> = (0..width).map(|x| x_min + x as f64 * (x_max - x_min) / width as f64).collect();
        let imaginary_axis: Vec<f64> = (0..height).map(|y| y_min + y as f64 * (y_max- y_min) / height as f64).collect();

        let mut atlas = vec![vec![0; width]; height];

        for iy in 0..height {
            for ix in 0..width {
                let cx = real_axis[ix];
                let cy = imaginary_axis[iy];

                atlas[iy][ix] = count_iterations(cx, cy, max_iter);
            }
        }

        atlas
    }
}
