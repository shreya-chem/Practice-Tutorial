import os, sys
import numpy as np

def open_xyz(file_location):
    xyz_file = np.genfromtxt(fname=file_location, dtype='unicode', skip_header=2)
    natoms = len(xyz_file[:,0])
    symbols = xyz_file[:,0]
    data = xyz_file[:,1:]
    data = data.astype(np.float64)
    return symbols, data, natoms

#symbols, data, natoms = open_xyz(file_location)

def calculate_distance(atom1_coord, atom2_coord):
    """Calculate the distance between two three-dimensional points."""
    
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = np.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return bond_length_12

def bond_check(atom_distance, min_length, max_length):
    if atom_distance > min_length and atom_distance <= max_length:
        return True
    else:
        return False
    
def print_bonds(symbols, natoms, data):
    for i in range (natoms):
        for j in range (natoms):
            distance = calculate_distance(data[i],data[j])
            if bond_check(distance, 0, 1.5):
                if i<j:
                    print (F'{symbols[i]} to {symbols[j]} : {distance:.3f}')
                    
if __name__ == "__main__":
	if len(sys.argv) < 2:
		raise NameError("Incorrect input! Please specify a file to analyze.")
	xyz_file = sys.argv[1]
	symbols, data, natoms = open_xyz(xyz_file)

	print(F'Printing bonds for {xyz_file}:')
	print_bonds(symbols, natoms, data)
'''
file_location = os.path.join('..','data', 'benzene.xyz')
symbols, data, natoms = open_xyz(xyzfilename)

print(F'Printing bonds for benzene.')
print_bonds(symbols, natoms, data)
'''
