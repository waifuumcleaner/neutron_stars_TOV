# constants.py
# This module defines important physical and numerical constants used
# throughout the project.

import numpy as np

class PhysicalConstants:
    """
    A class to store fundamental physical constants used in the calculations.
    """
    
    # Sun's mass in kg
    M_sun = 1.989e30  
    
    # Gravitational constant in m^3 kg^-1 s^-2
    G = 6.67430e-11  
    
    # Speed of light in m/s
    c = 2.99792458e8  
    
    # Sun's Schwarzschild radius in meters
    R_S = 2 * G * M_sun / c**2  
    
    # Convert Schwarzschild radius to kilometers
    R_S_km = R_S / 1000  
    
    # Scaling constant for initial mass calculation
    gamma = M_sun * c**2 / (R_S**3)
    
phys_c = PhysicalConstants()


class NumericalParameters:
    """
    A class to store numerical parameters for solving the equations.
    """
    
    # Initial radius for integration (units of R_s)
    r0 = 1e-6  
    
    # Number of central pressure values to compute
    n_P = 100  
    
    # Pressure range for central pressure (adimensional)
    first_P = 4e-7
    last_P = 4e+2  
 
    log_first_P = np.log(first_P)
    log_last_P = np.log(last_P)

    # Maximum number of steps in the Runge-Kutta method
    max_rk4_steps = int(1e7)  
    
    # Step size (units of R_s)
    diff_eq_step = 5e-3

num_p = NumericalParameters()