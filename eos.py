# eos.py
# Contains the equation of state (EoS) employed in the project.
# Polytrope obtained from fit of a pure neutron star Fermi gas model,
# with both relativistic and non-relativistic behaviour.

import numpy as np

def eos_rho(P):
    """
    Compute mass density according to a Fermi Gas EOS for arbitrary relativity.
    
    Args:
    P: array-like or scalar, Pressure (adimensional)
    
    Returns:
    Density corresponding to the input pressure.
    If pressure is negative, returns a very small number to avoid unphysical values.
    """
    P = np.maximum(P, 1E-8)  
    return 0.871 * (P ** (3./5.)) + 2.867 * P
