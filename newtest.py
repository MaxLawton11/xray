import numpy as np
import matplotlib.pyplot as plt
import xraydb

# X-ray attenuation calculations
# inputs from web form
formula = 'Fe'  # material chemical formula
density = 7.88  # material density in gr/cm^3
thickness = 1.000000  # material thickness, in mm
energy = np.arange(100, 40000+50, 50)
#energy = np.arange(100, 100000+50, 50)

mu_array = xraydb.material_mu(formula, energy, density=density)

atten_length = 10.0 / mu_array

trans_fract = np.exp(-0.1*thickness*mu_array)
atten_fract = 1 - trans_fract

import spekpy as sp

s=sp.Spek(kvp=40,th=12)
# Filter the spectrum
#s.filter('Fe',1.0)
# Get energy values array and fluence arrays (return values at bin-edges)
karr, spkarr = s.get_spectrum(edges=True)
original_array = np.array(spkarr)

# Specify the number of items for smoothing
num_smoothed_items = len(energy)  # You can change this number as needed
new_indices = np.linspace(0, len(original_array) - 1, num_smoothed_items)
smoothed_array = np.interp(new_indices, np.arange(len(original_array)), original_array)
# print(len(smoothed_array))



import pandas as pd

data = {
    'energy':energy,
    'atten_length':atten_length,
    'trans_fract':trans_fract,
    'atten_fract':atten_fract,
    'distribution': smoothed_array
}

df = pd.DataFrame(data)
print(df)
df.to_csv('output.csv')