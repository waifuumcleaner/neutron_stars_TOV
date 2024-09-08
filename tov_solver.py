import numpy as np
import eos
from constants import phys_c
from scipy.integrate import solve_ivp

def rk4_gen(f, r0, y0, step, max_step):
    """
    General RK4 solver for differential equations.
    Parameters:
        f (function): Function returning derivatives.
        r0 (float): Initial radius.
        step (float): Step size.
        max_step (int): Maximum number of steps.
        y0 (array): Initial values for the differential equations.
    Returns:
        xs (array): Array of radius values.
        ys (array): Array of solution values.
    """
    xs = r0 + np.arange(max_step) * step
    ys = []
    
    yvals = y0.copy()
    for x in xs:
        if yvals[0] < 0:  # Stop when pressure crosses 0
            break
        ys.append(yvals.copy())
        k0 = step * f(x, yvals)
        k1 = step * f(x + step / 2, yvals + k0 / 2)
        k2 = step * f(x + step / 2, yvals + k1 / 2)
        k3 = step * f(x + step, yvals + k2)
        yvals += (k0 + 2 * k1 + 2 * k2 + k3) / 6
    
    return np.array(xs[:len(ys)]), np.array(ys)

def rk4_gen_scipy(f, r0, y0, step, max_step):
    """
    General RK4 solver for differential equations using SciPy's solve_ivp.
    Parameters:
        f (function): Function returning derivatives.
        r0 (float): Initial radius.
        step (float): Step size.
        max_step (int): Maximum number of steps.
        y0 (array): Initial values for the differential equations.
    Returns:
        xs (array): Array of radius values.
        ys (array): Array of solution values.
    """
    # Define the event function to stop integration when pressure < 0
    def event(t, y):
        return y[0]  # Return pressure
    event.terminal = True  # Stop the integration when the event is triggered

    t_span = (r0, r0 + max_step * step)

    sol = solve_ivp(
        fun=f,
        t_span=t_span,
        y0=y0,
        method='RK45',
        t_eval=np.arange(r0, r0 + max_step * step, step),
        events=event
    )

    return sol.t, sol.y.T


def tov_rel(r, y):
    """
    Relativistic TOV equations for pressure (P) and mass (m).
    Parameters:
        r (float): Radial coordinate.
        y (array): Current values of P and m.
    Returns:
        array: Derivatives [dP/dr, dm/dr].
    """    
    P, m = y
    rho = eos.eos_rho(P)
    
    dP_dr = - (m * rho / (2 )) * (1 + P/rho) * (1 + 4 * np.pi * (r**3) * P / m) * (1/(r**2-m*r))
    dm_dr = 4 * np.pi * (r**2) * rho
    
    return np.array([dP_dr, dm_dr])

def tov_non_rel(r, y):
    """
    Non-relativistic equations for pressure (P) and mass (m).
    
    Parameters:
        r (float): Radial coordinate.
        y (array): Current values of P and m.
        
    Returns:
        array: Derivatives [dP/dr, dm/dr].
    """
    P, m = y
    rho = eos.eos_rho(P)
    
    dP_dr = - (m * rho / (2 * r**2))
    dm_dr = 4 * np.pi * (r**2) * rho
    
    return np.array([dP_dr, dm_dr])

def get_M0(r_delta, rho_c):
    """
    Computes initial mass of the star.

    Parameters:
        r_delta (float): Initial star radius (close to 0).
        rho_c (float): Initial central density.
    """
    m_delta0 = (4/3*np.pi*(r_delta*phys_c.R_S_km)**3*(rho_c*phys_c.gamma/phys_c.c**2))/phys_c.M_sun
    return m_delta0