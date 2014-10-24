import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2 or sys.argv[1] == 'help' or sys.argv[1] == 'h' or sys.argv[1] == '--help':
    print "Usage: python dataanalysis.py <filename> [molecule]"
    quit()

# Define Constants
h = 4.135667e-15        # Planck's constant in eV*s
c = 299792458e9         # Speed of Light in nm/s
me = 5.10998910e-11     # Electron Mass in eV/c^2 where c is in nm

# Set Data filename and molecule name
filename = sys.argv[1]
if len(sys.argv) == 3:
    molecule = sys.argv[2]
else:
    molecule = filename


# Define HOMO Levels Depending on Molecule
if 'naphthalene' in molecule.lower():
    HOMO = 5
    lmultx = 2
    lmulty = 1
elif 'anthracene' in molecule.lower():
    HOMO = 7
    lmultx = 3
    lmulty = 1
elif 'tetracene' in molecule.lower():
    HOMO = 9
    lmultx = 4
    lmulty = 1
else:
    print("No defined HOMO level for {0}. Exiting...".format(molecule))
    quit()

# Define LUMO Level
LUMO = HOMO + 1

# Molecule Data
print("Molecule: {0}".format(molecule))
print("HOMO Level: {0}".format(HOMO))
print("LUMO Level: {0}".format(LUMO))

with open(filename, 'rb') as datafile:
    # Get data
    data = csv.reader(datafile, delimiter=',')

    # Assign data appropriately
    wavelength = []
    absorption = []
    for row in data:
        # Throw away beginning peak
        if(float(row[0]) >= 200):
            wavelength.append(float(row[0]))
            absorption.append(float(row[1]))

# Max Wavelength Needed for Analysis
maxAbsIndex = absorption.index(max(absorption))
maxWavelength = wavelength[maxAbsIndex]
print("Wavelength of max absorption: {0} nm".format(maxWavelength))

# Energy Gap
# E = hc/lambda
E = h*c/maxWavelength
print("Energy gap: {0} eV".format(E))

# Get Energy Level Transition
L = np.sqrt((h**2*LUMO**2)/(8*me*E))
print("Molecule Length: {1}".format(molecule, L))


# Plot wavelength/absorption
plt.plot(wavelength, absorption)
plt.title("Wavelength vs. Absorption for {0}".format(molecule), fontsize=20)
plt.axis([min(wavelength), max(wavelength), min(absorption), max(absorption)])
plt.xlabel(r"$\lambda$ (nm)", fontsize=16)
plt.ylabel(r"$\log \epsilon$", fontsize=16)
plt.show()
