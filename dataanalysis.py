import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2 or sys.argv[1] == 'help' or sys.argv[1] == 'h' or sys.argv[1] == '--help':
    print "Usage: python dataanalysis.py <filename1> <molecule1> ... <filenameN> <moleculeN>"
    quit()

# Define Constants
h = 4.135667e-15        # Planck's constant in eV*s
c = 299792458e9         # Speed of Light in nm/s
me = 5.10998910e-11     # Electron Mass in eV/c^2 where c is in nm

# Set Data filename and molecule name
filename = []
molecule = []

for i in range(1, len(sys.argv)):
  if i % 2 == 0:
    molecule.append(sys.argv[i])
  else:
    filename.append(sys.argv[i])

# Declare Arrays
HOMO = []
LUMO = []
wavelength = []
absorption = []

# Make Figure
fig = plt.figure()

# Declare Plots
plots = []

for m in range(0, len(molecule)):
  print
  # Define HOMO Levels Depending on Molecule
  if 'naphthalene' in molecule[m].lower():
      HOMO.append(5)
  elif 'anthracene' in molecule[m].lower():
      HOMO.append(7)
  elif 'tetracene' in molecule[m].lower():
      HOMO.append(9)
  else:
      print("No defined HOMO level for {0}. Exiting...".format(molecule[m]))
      quit()

  # Define LUMO Level
  LUMO.append(HOMO[m] + 1)

  # Molecule Data
  print("Molecule: {0}".format(molecule[m]))
  print("HOMO Level: {0}".format(HOMO[m]))
  print("LUMO Level: {0}".format(LUMO[m]))

  with open(filename[m], 'rb') as datafile:
      # Get data
      data = csv.reader(datafile, delimiter=',')

      # Assign data appropriately
      wavelength.append([])
      absorption.append([])
      for row in data:
          # Throw away beginning peak and ending zeros
          if float(row[0]) >= 200 and float(row[0]) <= 500:
              wavelength[m].append(float(row[0]))
              absorption[m].append(float(row[1]))

  # Max Wavelength Needed for Analysis
  maxAbsIndex = absorption[m].index(max(absorption[m]))
  maxWavelength = wavelength[m][maxAbsIndex]
  print("Wavelength of max absorption: {0} nm".format(maxWavelength))

  # Energy Gap
  # E = hc/lambda
  E = h*c/maxWavelength
  print("Energy gap: {0} eV".format(E))

  # Get Energy Level Transition
  L = np.sqrt((h**2*LUMO[m]**2)/(8*me*E))
  print("Molecule Length: {0}".format(L))

  # Create Subplot for this data
  plots.append(fig.add_subplot(111))

  # Plot Data
  plots[m].plot(wavelength[m], absorption[m], label=molecule[m])


# Plot wavelength/absorption
plt.title("Wavelength vs. Absorption", fontsize=20)
#plt.axis([min(wavelength), max(wavelength), min(absorption), max(absorption)])
plt.xlabel(r"$\lambda$ (nm)", fontsize=16)
plt.ylabel(r"$\log \epsilon$", fontsize=16)
plt.legend()
plt.show()
