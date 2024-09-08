import numpy as np
from constants import num_p
import tov_solver

def compute_solutions(P_c, rho_c, use_scipy=False):
    """
    Solve the TOV equations for both relativistic and non-relativistic cases.

    Parameters:
        P_c (float): Central pressure.
        rho_c (float): Central density.
        use_scipy (bool): If True, use SciPy's solve_ivp; otherwise, use the custom RK4 solver.

    Returns:
        tuple: Two tuples containing:
            - (masses_rel, radii_rel, pressures_rel): Relativistic case results.
            - (masses_nonrel, radii_nonrel, pressures_nonrel): Non-relativistic case results.
    """
    m0 = tov_solver.get_M0(num_p.r0, rho_c)
    y0 = np.array([P_c, m0])

    equations = [tov_solver.tov_rel, tov_solver.tov_non_rel]
    results = []

    for eq in equations:
        if use_scipy:
            radii, results_case = tov_solver.rk4_gen_scipy(
                eq, num_p.r0, y0, num_p.diff_eq_step, num_p.max_rk4_steps
            )
        else:
            radii, results_case = tov_solver.rk4_gen(
                eq, num_p.r0, y0, num_p.diff_eq_step, num_p.max_rk4_steps
            )
        results.append((radii, results_case[:, 0], results_case[:, 1]))

    (radii_rel, pressures_rel, masses_rel), (radii_nonrel, pressures_nonrel, masses_nonrel) = results

    return (masses_rel, radii_rel, pressures_rel), (masses_nonrel, radii_nonrel, pressures_nonrel)
