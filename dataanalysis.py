import sys
import csv
import matplotlib.pyplot as plt

if(len(sys.argv) != 2):
    print "Usage: python dataanalysis.py <filename>"
    quit()

# Set Data filename
filename = sys.argv[1]

with open(filename, 'rb') as file:
    # Get data
    data = csv.reader(file, delimiter=',')

    # Assign data appropriately
    wavelength = []
    absorption = []
    for row in data:
        wavelength.append(float(row[0]))
        absorption.append(float(row[1]))

plt.plot(wavelength, absorption)
plt.show()


