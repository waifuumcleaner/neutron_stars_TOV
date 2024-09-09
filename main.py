# main.py
# This module contains the main function for the execution of the program.

import numpy as np
from constants import num_p, phys_c
import utils
import eos
import argparse
from time_performance import time_test
from tov_calculations import compute_solutions
import plotting as pt

def main():
    """
    Main function to solve TOV equations and plot results.
    Handles command-line arguments, performs computations, and generates plots.
    """
    parser = argparse.ArgumentParser(description="TOV solver")
    parser.add_argument('--time_test', action='store_true', help="Estimate execution time")
    parser.add_argument('--use_scipy', action='store_true', help="Use SciPy's solve_ivp instead of custom RK4")
    args = parser.parse_args()

    if args.time_test:
        P_c = 0.001  # Example central pressure for timing test
        Rho_c = eos.eos_rho(P_c)
        average_ex_time = time_test(compute_solutions, P_c, Rho_c, use_scipy=args.use_scipy)
        print(f"Execution time: {average_ex_time:.2f} ms")
    else:
        # Generate central pressures and corresponding densities
        exponents = utils.rescaled_exponents(num_p.log_first_P, num_p.log_last_P, num_p.n_P, power=1.0)
        central_pressures = np.exp(exponents)
        central_rhos = eos.eos_rho(central_pressures)

        # Initialize arrays to store results
        final_masses_rel = np.zeros_like(central_pressures)
        final_radii_rel = np.zeros_like(central_pressures)
        final_masses_nonrel = np.zeros_like(central_pressures)
        final_radii_nonrel = np.zeros_like(central_pressures)

        all_radii = []
        all_pressures = []
        all_densities = []

        target_pressure = 0.001
        nearest_idx = np.abs(central_pressures - target_pressure).argmin()

        for i, P_c in enumerate(central_pressures):
            (masses_rel, radii_rel, pressures_rel), (masses_nonrel, radii_nonrel, pressures_nonrel) = compute_solutions(
                P_c, central_rhos[i], use_scipy=args.use_scipy
                )
            
            # Convert radii from units to kilometers
            radii_rel *= phys_c.R_S_km
            radii_nonrel *= phys_c.R_S_km

            # Store final results (i.e., when P = 0) for the current central pressure
            final_masses_rel[i] = masses_rel[-1]
            final_radii_rel[i] = radii_rel[-1]
            final_masses_nonrel[i] = masses_nonrel[-1]
            final_radii_nonrel[i] = radii_nonrel[-1]

            # Collect data for 3D plotting
            all_radii.extend(radii_rel)
            all_pressures.extend(pressures_rel / (phys_c.R_S_km**3))  
            all_densities.extend(np.full_like(radii_rel, np.log10(central_rhos[i] / (phys_c.R_S_km**3))))

            # Plot profiles for a specific central pressure
            if i == nearest_idx:
                pt.plot_pressure_profile(target_pressure, radii_rel, pressures_rel, radii_nonrel, pressures_nonrel)
                pt.plot_mass_profile(target_pressure, radii_rel, masses_rel, radii_nonrel, masses_nonrel)

        # Generate final plots
        pt.plot_pressure_surface(all_radii, all_pressures, all_densities, show=True)
        pt.plot_mass_radius_relation(final_radii_rel, final_masses_rel)
        pt.plot_mass_radius_relation(final_radii_rel, final_masses_rel, final_radii_nonrel, final_masses_nonrel)
        pt.plot_density_pressure_relation(central_pressures, central_rhos)

if __name__ == "__main__":
    main()
