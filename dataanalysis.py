import sys
import csv
import matplotlib.pyplot as plt

if len(sys.argv) != 2 or sys.argv[1] == 'help' or sys.argv[1] == 'h' or sys.argv[1] == '--help':
    print "Usage: python dataanalysis.py <filename>"
    quit()

# Define Constants
h = 4.135667e-15    # Planck's constant in eV*s
c = 299792458e9    # Speed of Light in nm/s


# Set Data filename
filename = sys.argv[1]

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
# Assuming this means wavelength of max absorption
maxAbsIndex = absorption.index(max(absorption))
maxWavelength = wavelength[maxAbsIndex]
print("Maximum wavelength: {0}".format(maxWavelength))

# Energy Gap
# E = hc/lambda
E = h*c/maxWavelength
print("Energy gap: {0} eV".format(E))


plt.plot(wavelength, absorption)
plt.show()


