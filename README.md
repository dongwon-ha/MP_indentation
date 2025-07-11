# MP_indentation
Python script for the material property optimization of microparticles


- Consists of three parts:
    (1) Hertz Model Fitting (hertz_model_fit): Fit Hertz model to the experimental data
    (2) Grid Search (grid_search): An error surface was constructed over a grid of material properties (Young’s modulus and Poisson’s ratio) by computing the RMSE between simulated and experimental force–displacement data.
    (3) Optimization (optimization): Optimization was carried out over Young's modulus and Poisson's ratio, minimizing RMSE

