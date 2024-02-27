# For compatibility with Python2
from __future__ import print_function, division, absolute_import
#

import spekpy as sp
try:
    from matplotlib import pyplot as plt
except:
    print("Cannot import matplotlib. Please check that it is installed")
print("\n** Script to generate a filtered spectrum and plot using matplotlib **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=40,th=12)
# Filter the spectrum
#s.filter('Fe',1.0)
# Get energy values array and fluence arrays (return values at bin-edges)
karr, spkarr = s.get_spectrum(edges=True)
print(len(karr))
# Plot spectrum
plt.plot(karr, spkarr)
plt.xlabel('Energy [keV]')
plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
plt.title('An example x-ray spectrum')
plt.show()