from matplotlib import pyplot as plt
import brems

energy = 30

# Plot brems spectrum
specs = brems.spectrum(energy)
plt.plot(specs["karr"], specs["spkarr"], color='blue')
plt.title(f"Brems X-Ray Spectrum ({energy} keV)")
plt.xlabel("Energy [keV]")
plt.ylabel("Fluence [photons/cm²/mAs/keV]")

plt.show()
