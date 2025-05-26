from matplotlib import pyplot as plt
import atten

energy = 100
element = 'Fe'
thickness = 2

# Plot transmission
trans = atten.transmission(element, thickness, 100, energy)

plt.plot(trans["energies"], trans["transmission_per"], color='orange')
plt.title(f"Transmission Through {element} ({thickness:.2f} mm)")
plt.xlabel("Energy (eV)")
plt.ylabel("Transmission (%)")
plt.yscale('linear')
plt.ylim(0, 100)

plt.show()
