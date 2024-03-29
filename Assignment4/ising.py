# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy,
# and Chris Florencio-Aleman
# Homework 7, PP10

import sys
import random
import array_plot


def spin_periodic(array, x_coord, y_coord):
    '''Part 2: return spin in specified cell of array, wrapping around if
    out of bounds.
    '''
    (side_x, side_y) = array.shape
    return array[x_coord % side_x][y_coord % side_y]


def energy(array):
    '''Part 3: calculate total energy normalized to J of a system
    defined by an array.

    array: ising model array to consider

    Returns: total energy of system normalized to J
    '''
    [rows, columns] = array.shape

    energy = 0

    # Iterate over each cell
    for i in range(rows):
        for j in range(columns):
            # Compare with values of cells to right and below
            spin_ij = array[i][j]
            neighbors = [spin_periodic(array, i, j+1), spin_periodic(array, i+1, j)]

            # Add to energy if different, subtract if same
            for neighbor_spin in neighbors:
                if spin_ij == neighbor_spin:
                    energy -= 1
                else:
                    energy += 1

    return energy


def local_energy(array, i, j):
    '''Calculate the local energy for a single spin and its neighbors.

    array: ising model array to consider
    i, j: indices of cell to analyze

    Returns: local energy of spin and neighbors normalized to J
    '''
    energy = 0
    spin_ij = spin_periodic(array, i, j)
    # Check neighbors above, below, left, and right of selected spin
    neighbors = [spin_periodic(array, i, j+1), spin_periodic(array, i, j-1),
                 spin_periodic(array, i-1, j), spin_periodic(array, i+1, j)]

    # Add to energy if different, subtract if same
    for neighbor_spin in neighbors:
        if spin_ij == neighbor_spin:
            energy -= 1
        else:
            energy += 1

    return energy


def pick_spin(array, i, j, T):
    '''Part 4: choose to flip a spin or keep it in original state.

    array: ising model array to consider
    i, j: indices of cell with spin to pick
    T: temperature (multiple of J)

    Returns: spin picked for array[i][j]
    '''
    energy = local_energy(array, i, j)
    array[i][j] = int(not array[i][j])
    energy_flipped = local_energy(array, i, j)
    if energy_flipped < energy:
        return array[i][j]
    else:
        # Compare random number between 0 and 1 to boltzmann probability
        E_difference = energy - energy_flipped
        if random.random() > array_plot.boltzmann(E_difference, T):
            # Return array with flipped spin
            return array[i][j]
        else:
            # Restore original spin
            return int(not array[i][j])


if __name__ == "__main__":
    '''Part 6: main routine

    Initializes a random array, then randomly selects spins in
    the configuration, flips them and chooses whether to accept
    the change or not.
    '''
    try:
        dimension = int(sys.argv[1])
        T = float(sys.argv[2])
    except:
        print "Please run with arguments: ising.py <dimension of array> <temperature>"
        sys.exit()

    array = array_plot.create_random_array(dimension)

    # For 1e6 samples, randomly select spin in configuration,
    # flip spin and decide whether or not to accept change
    for k in range(int(1e6)):
        i = int(random.random() * dimension)
        j = int(random.random() * dimension)
        array[i][j] = pick_spin(array, i, j, T)

    array_plot.plot_array(array, "Ising model with T = %.1fJ" % T)
