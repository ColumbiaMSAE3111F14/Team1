# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy,
# and Chris Florencio-Aleman
# Homework 7, PP10

import sys
import random
import array_plot
import math as m
import numpy as np
import matplotlib.pyplot as plt

k = 1.3806488 * m.pow(10,-23)

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


def get_N_up(array):
    '''Returns the number of up cells in teh array'''
    total = 0
    for row in array:
        for cell in row:
            total += cell
    return total

def get_order(array):
    '''Compute order using formula |N_up-N_down|/N'''
    N_up = float(get_N_up(array))
    N = float(array.shape[0]*array.shape[1])
    return abs(N-2*N_up)/N

def iterate(array, T):
    '''Runs pick_spin on a random cell of an array.
    This function as an iteration of the simulation.
    Returning whether the iteration results in a change is useful for equilibrium checks.
    '''
    i = int(random.random() * array.shape[0])
    j = int(random.random() * array.shape[1])
    old_value = array[i][j]
    array[i][j] = pick_spin(array, i, j, T)
    return old_value == array[i][j]

def run_to_equilibrium(array, T, e):
    '''Run the array at tempurature T until no changes occur for e iterations.'''
    count = 0 #Iterations since last change
    i = 0
    while (count < e):
        if iterate(array, T):
            count +=1
        else:
            i+=1
            count = 0
    return array

def calc_entropy(array):
    '''Calculates and returns entropy for spin system using Boltzmann relation'''
    N_up = get_N_up(array)
    N = array.shape[0]*array.shape[1]
    g = m.factorial(N)/(m.factorial(N_up)*m.factorial(N-N_up))
    entropy = k * m.log(g)
    return entropy

if __name__ == "__main__":
    '''Part 6: main routine

    Initializes a random array, then randomly selects spins in
    the configuration, flips them and chooses whether to accept
    the change or not.
    '''
    try:
        dimension = int(sys.argv[1])
    except:
        print "Please run with arguments: ising.py <dimension of array>"
        sys.exit()

    temps = np.arange(0.1, 6.1, 0.1)
    orders = []
    orig = array_plot.create_random_array(dimension)
    for temp in temps:
        array = orig
        staticness = 0
        while True:
            if iterate(array, temp):
                staticness += 1
            else:
                staticness = 0
            if staticness > 100000:
                orders.append(get_order(array))
                print "Got order parameter for %f" % temp
                break

    plt.figure()
    plt.plot(temps, orders, '.')
    plt.title("Order parameter and temperature")
    plt.xlabel("Temperature (J)")
    plt.ylabel("Order parameter")
    plt.show()

