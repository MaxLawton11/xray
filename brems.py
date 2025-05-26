import spekpy as sp
from matplotlib import pyplot as plt


def spectrum(kvp) : 
    # Generate unfiltered spectrum
    s=sp.Spek(kvp,th=12,dk=0.4)
    # Filter the spectrum
    #s.filter('Fe',1.0)
    # Get energy values array and fluence arrays (return values at bin-edges)
    karr, spkarr = s.get_spectrum(edges=True)
    return { "karr":karr, "spkarr": spkarr}

# plt.xlabel('Energy [keV]')
# plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
# plt.title('An example x-ray spectrum')
# plt.show()