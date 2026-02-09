use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod py_mandelbrot_rs {
    use pyo3::prelude::*;
    use num::Complex;
    use rayon::prelude::*;
    
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
        let x_values: Vec<f64> = (0..width).map(|x| x as f64 * (x_max - x_min) / width as f64).collect();
        let y_values :Vec<f64> = (0..height).map(|y| y as f64 * (y_max - y_min) / height as f64).collect();

        (0..height).into_par_iter().map(|y| 
            (0..width).map(|x| 
                mandelbrot_iterate(x_values[x], y_values[y], max_iter)).collect()).collect()
    }
}
