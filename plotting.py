# plotting.py
# This module contains the functions to produce all relevant plots for the program.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from scipy.interpolate import griddata

def plot_pressure_surface(all_radii, all_pressures, all_densities, colormap='plasma', threshold=2.5e-10, show=False):
    """
    Plot a 3D surface of pressure as a function of radius and central density.
    """
    radii_grid, density_grid = np.meshgrid(
        np.linspace(min(all_radii), max(all_radii), num=50),
        np.unique(all_densities)
    )
    # Pressure values below the threshold are uniformly clamped to smooth the bottom of the surface
    log_pressures = np.log10(all_pressures)
    log_pressures[log_pressures < np.log10(threshold)] = np.log10(threshold)

    pressures_grid = griddata(
        (all_radii, all_densities), 
        log_pressures, 
        (radii_grid, density_grid), 
        method='linear'
    )
    pressures_grid = np.nan_to_num(pressures_grid, nan=np.log10(threshold))
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    norm = mcolors.PowerNorm(gamma=0.4, vmin=np.log10(threshold), vmax=np.log10(np.max(all_pressures)))
    ax.plot_surface(
        radii_grid, density_grid, pressures_grid, 
        cmap=colormap, norm=norm, linewidth=0, antialiased=False
    )
    ax.set_xlabel('Radius (km)')
    ax.set_ylabel(r'Central Density [$log_{10}(M_s / km^3)$]')
    ax.set_zlabel(r'Pressure [$log_{10}(M_s c^2 / km^3)$]')
    ax.set_title('Pressure as a Function of Radius and Central Density')
    ax.view_init(elev=15, azim=-25)
    plt.tight_layout()
    plt.savefig("outputs/P_profile_3D.png")

    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_mass_radius_relation(final_radii_rel, final_masses_rel, final_radii_nonrel=None, final_masses_nonrel=None, show=False):
    """
    Plot the mass-radius relation for neutron stars, comparing relativistic and non-relativistic cases if provided.
    """
    fig = plt.figure(figsize=(10, 7))
    plt.plot(final_radii_rel, final_masses_rel, 'o-', color='darkred', label='Relativistic', markersize=8)
    
    if final_radii_nonrel is not None and final_masses_nonrel is not None:
        plt.plot(final_radii_nonrel, final_masses_nonrel, 'o--', color='royalblue', label='Non-relativistic', markersize=8)
        output_filename = "outputs/M_vs_R_comparison.png"
    else:
        output_filename = "outputs/M_vs_R_rel.png"
    
    plt.xlabel('Radius (km)', fontsize=14)
    plt.ylabel(r'Mass ($M_s$)', fontsize=14)
    plt.title('Mass-Radius Relation for Neutron Stars', fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_filename)
    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_density_pressure_relation(central_pressures, central_rhos, show=False):
    """
    Plot the density-pressure relation with log-log scaling for neutron stars.
    """
    fig = plt.figure(figsize=(10, 7))
    plt.plot(central_pressures, central_rhos, 
             'o-', color='mediumblue', label='Density vs Pressure', markersize=8)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'Pressure ($M_s c^2/R_s^3$)', fontsize=14)
    plt.ylabel(r'Density ($M_s/R_s^3$)', fontsize=14)
    plt.title('Density-Pressure Relation for Neutron Stars', fontsize=16)
    plt.grid(True, which="both", linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("outputs/Rho_vs_P.png")
    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_pressure_profile(target_pressure, radii_for_target_rel, pressures_for_target_rel, radii_for_target_nonrel=None, pressures_for_target_nonrel=None, show=False):
    """
    Plot the pressure profile for the specified target pressure.
    """
    fig = plt.figure(figsize=(10, 7))
    if radii_for_target_rel is not None and pressures_for_target_rel is not None:
        plt.plot(radii_for_target_rel, pressures_for_target_rel, 'o-', color='royalblue', label='Relativistic', markersize=4)
    if radii_for_target_nonrel is not None and pressures_for_target_nonrel is not None:
        plt.plot(radii_for_target_nonrel, pressures_for_target_nonrel, 'o-', color='darkred', label='Non-relativistic', markersize=4)
    plt.xlabel('Radius (km)', fontsize=14)
    plt.ylabel(r'Pressure ($M_s c^2 / R_s^3$)', fontsize=14)
    plt.title(f'Pressure Profile for Central Pressure ~ {target_pressure:.3f}', fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("outputs/P_profile.png")
    if show:
        plt.show()
    else:
        plt.close(fig)

def plot_mass_profile(target_pressure, radii_rel, masses_rel, radii_nonrel=None, masses_nonrel=None, show=False):
    """
    Plot the mass profile for the specified target pressure.
    """
    fig = plt.figure(figsize=(10, 7))
    if radii_rel is not None and masses_rel is not None:
        plt.plot(radii_rel, masses_rel, 'o-', color='royalblue', label='Relativistic', markersize=4)
    if radii_nonrel is not None and masses_nonrel is not None:
        plt.plot(radii_nonrel, masses_nonrel, 'o-', color='darkred', label='Non-relativistic', markersize=4)
    plt.xlabel('Radius (km)', fontsize=14)
    plt.ylabel(r'Mass ($M_s$)', fontsize=14)
    plt.title(f'Mass Profile for Central Pressure ~ {target_pressure:.3f}', fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("outputs/M_profile.png")
    if show:
        plt.show()
    else:
        plt.close(fig)