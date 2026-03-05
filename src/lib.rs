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

    fn range(start: f64, stop: f64, count: usize) -> Vec<f64> {
        let step = (stop - start) / count as f64;
        (0..count)
            .map(|n| (n as f64).mul_add(step, start))
            .collect()
    }

    #[pyfunction]
    fn calculate_mandelbrot(x_min: f64, x_max: f64, y_min: f64, y_max: f64, width: usize, height: usize, max_iter: u32) 
            -> Vec<Vec<u32>> {
        let xrange = range(x_min, x_max, width);
        let yrange = range(y_min, y_max, height);

        (0..height)
            .into_par_iter() // distribute row computations between cpu cores using rayon
            .map(|y| {
                (0..width)
                    .map(|x| {
                        mandelbrot_iterate(xrange[x], yrange[y], max_iter)
                    })
                    .collect()
            })
            .collect()
    }
}
