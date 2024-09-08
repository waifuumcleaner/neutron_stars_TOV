# Tolman-Oppenheimer-Volkoff Equations

## Overview

This project solves the Tolman-Oppenheimer-Volkoff (TOV) equations to model neutron stars. In particular it calculates the final mass and radius of neutron stars starting from different values of central pressure. Both non-relativistic and relativistic equations are employed, and the result is compared. The code produces also the behaviour of the pressure and mass in function of the radius for a certain value of the initial pressure. The equations are solved numerically implementig the fourth order Runge-Kutta method. It is also possible to estimate the execution time of the method. The project follows the exercise proposed in [this book](#references).

## Tolman-Oppenheimer-Volkoff Equations

The differential equations that describe the variations of mass and pressure for a neutron star in function of the redius are the following:

$$ \frac{dM}{dr} = 4 \pi r^2 \rho(r)
$$

$$ \frac{dP}{dr} = -\frac{G M(r)}{r^2} \rho(r)
$$

where G is the gravitational constant and rho(r) the density.

Including also relativity corrections, the equation of the pressure takes the form: 

$$ \frac{dP(r)}{dr} = \frac{G M(r) \rho(r)}{r^2} \left[ 1 + \frac{P(r)}{\rho(r) c^2} \right] \left[ 1 + \frac{4 \pi r^3 P(r)}{M(r) c^2} \right] \left[ 1 - \frac{2 G M(r)}{c^2 r} \right]^{-1}
$$

where $c^2$ is the speed of light.

For r=0 the mass is 0 and the maximum value of r and since the pressure of a neutron star vanishes at the surface, the maximum value of r and M is reached when P = 0.

The equation of state used to express the relation between P and $\rho$ is the one suggested by [1](#references):

$$ \bar{\rho} = 0.871 \bar{P}^{3/5} + 2.667 \bar{P}
$$

where $\rho = \bar{\rho} \frac{M_s}{R_s^3}$ and $P = \bar{P} \frac{M_s}{R_s^3} c^2$ with $M_s$ and $R_s$ are the mass and the radius of the sun. This equation has been empirically obtained, starting from the Fermi gas model, to take into account both non-relativistic and relativistic effects. 

## Project File Description
constants.py eos.py tov_solver.py utils.py 
- **[`constants.py`](./constants.py)**: Contains all the physical constants and all the parameters of the simulation.
- **[`eos.py`](./eos.py)**: Contains the equation of state employed in the project.
- **[`tov_solver.py`](./tov_solver.py)**: Contains the equations to be solved, the non-relativistic and relativistic one.
- **[`rk4.py`](./rk4.py)**: Implements the fourth-order Runge-Kutta method for solving differential equations.
- **[`utils.py`](./utils.py)**: Contains utility functions for operations across the project.
- **[`time_performance.py`](./time_performance.py)**: Contains a function to estimate execution time of the rk4 method
- **[`output/`](./output)**: Directory where result plots are saved.

## Requirements

This code is written in **Python** and needs the following Python libraries:

- NumPy
- SciPy
- Matplotlib

## Run the project

You can run the code using the `Makefile`. 

-To run the main script:

   ```bash
   make run
   ```
   
-To measure the execution time:

   ```bash
   make time_test
   ```

-To get a list of all run options:

   ```bash
   make help
   ```

## References

1. Gezerlis, A. (2023b). Numerical Methods in Physics with Python (2nd ed., Chap. 8). Cambridge University Press.
