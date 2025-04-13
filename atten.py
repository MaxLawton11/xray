import numpy as np
import matplotlib.pyplot as plt
import xraydb

def transmission(element, thickness_mm, steps, kev_max, kev_min=1) :

    # Material properties
    element = element
    density = xraydb.atomic_density(element)  # g/cm³

    # Thickness in mm
    thickness_mm = thickness_mm
    thickness_cm = thickness_mm * 0.1  # convert to cm

    # Energy range in eV
    energies = np.linspace(kev_min*1000, kev_max*1000, steps)  # 1 keV to 30 keV

    # Mass attenuation coefficients (cm²/g)
    mu = xraydb.mu_chantler(element, energies)

    # Transmission using Beer-Lambert Law
    transmission_per = np.exp(-mu * density * thickness_cm) * 100  # in %

    return {"energies": energies, "transmission_per":transmission_per}

    # # Plotting
    # plt.figure(figsize=(9, 5))
    # plt.plot(energies, transmission_per, color='navy', label=f'{element}, {thickness_mm:.2f} mm')
    # plt.xlabel('Energy (eV)')
    # plt.ylabel('Transmission (%)')
    # plt.title(f'X-ray Transmission Through {element} ({thickness_mm:.2f} mm thick)')
    # plt.grid(True)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()
