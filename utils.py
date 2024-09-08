import numpy as np

def rescaled_exponents(start, end, n, power=2.0):
    """
    Generate rescaled exponents to skew the pressure point distribution.
    
    Args:
    start (float): log of the first pressure.
    end (float): log of the last pressure.
    n (int): number of points.
    power (float): the power used for the rescaling. Higher values will 
                   concentrate points near the lower end.
    
    Returns:
    np.array: array of rescaled exponents.
    """
    linear_space = np.linspace(0, 1, n)
    rescaled_space = linear_space ** power
    
    # Map back to the original range
    exponents = start + (end - start) * rescaled_space
    return exponents
