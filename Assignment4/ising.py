# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy,
# and Chris Florencio-Aleman
# Homework 7; PP10

import array_plot
import random
import sys

def ising():
    '''Part 6: main routine

    Initializes a random array, then randomly selects spins in
    the configuration, flips them and chooses whether to accept
    the change or not.

    To run from command line: python ising.py dimension_of_array temperature

    Returns: nothing'''
    try:
        n = int(sys.argv[1])
        T = float(sys.argv[2])
    except:
        print "invalid input"
        sys.exit()
        
    array = array_plot.create_random_array(n, 0.5)
    array_plot.plot_array(array, "Ising Model")
    for k in range(1000000):
        i = int(random.random() * n)
        j = int(random.random() * n)
        array = pick_spin(array, i, j, T)
              
    array_plot.plot_array(array, "Ising Model")
    

def spin_periodic(array, x_coord, y_coord):
    '''Part 2: return spin in a cell, wrapping around if out of bounds.'''
    (side_x, side_y) = array.shape
    return array[x_coord % side_x][y_coord % side_y]

def energy(array):
    '''Part 3: return the total energy normalized to J of a system
    defined by an array.'''
    [rows, columns] = array.shape

    energy = 0 #Start energy at 0 before totalling.

    #Iterate over each cell
    for i in range(rows):
        for j in range(columns):
            #Compare with values of cells to right and below.
            cell = array[i][j]
            cell_to_right = spin_periodic(array, i, j+1)
            cell_below = spin_periodic(array, i+1, j)

            #Add to energy if different. Subtract if same.
            if (cell == cell_to_right):
                energy -= 1
            else:
                energy += 1
            if (cell == cell_below):
                energy -= 1
            else:
                energy +=1

    return energy

def local_energy(array, i, j):
    '''Calculates the local energy for a single position which can
    be used to find the change in energy from flipping a position'''
    energy = 0
    cell = spin_periodic(array, i, j)
    cell_to_right = spin_periodic(array, i, j+1)
    cell_to_left = spin_periodic(array, i, j-1)
    cell_below = spin_periodic(array, i-1, j)
    cell_above = spin_periodic(array, i+1, j)

    if(cell == cell_to_right):
        energy -= 1
    else:
        energy += 1
    if(cell == cell_to_left):
        energy -= 1
    else:
        energy += 1
    if(cell == cell_above):
        energy -= 1
    else:
        energy += 1
    if(cell == cell_below):
        energy -= 1
    else:
        energy += 1

    return energy
    
def pick_spin(array, i, j, T):
    '''Part 4: chooses to flip a position or keep it in original state'''
    energy = local_energy(array, i, j)
    array[i][j] = not array[i][j]
    energy_flipped = local_energy(array, i, j)
    if energy > energy_flipped:
        return array
    else:
        E = energy - energy_flipped
        a = random.random()
        b = array_plot.boltzmann(E,T)
        if a > b:
            return array
        else:
            array[i][j] = not array[i][j]
            return array

ising()
