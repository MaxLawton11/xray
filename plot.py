import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("output.csv")
print(df)
formula = 'Fe'

plt.subplot(1,3, 1)
plt.plot(df['energy'], df['trans_fract'], label='Transmitted %', color='green')
plt.plot([35_000, 35_000], [0,max(df['trans_fract'])], color='orange')
plt.xlabel('Energy [eV]')
plt.ylabel('Tranmitted Fraction')
plt.title('Transmission for %s' % formula)
plt.legend()

plt.subplot(1,3, 2)
plt.plot(df['energy'], df['distribution'], label='Distribution', color='red')
plt.plot([35_000, 35_000], [0,max(df['distribution'])], color='orange')
plt.xlabel('Energy [eV]')
plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
plt.title('X-ray spectrum for %s' % formula)

plt.subplot(1,3, 3)
plt.plot(df['energy'], df['distribution']*df['trans_fract'], label='Distribution', color='blue')
plt.plot([35_000, 35_000], [0,max(df['distribution']*df['trans_fract'])], color='orange')
plt.xlabel('Energy [eV]')
plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()