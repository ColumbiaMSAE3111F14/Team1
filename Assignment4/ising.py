import array_plot
import random

def spin_periodic(array, x_coord, y_coord):
    '''Part 2: return spin in a cell, wrapping around if out of bounds.'''
    (side_x, side_y) = array.shape
    return array[x_coord % side_x][y_coord % side_y]

def energy(array):
    '''Part 3: return the total energy normalized to J of a system defined by an array.'''
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

def pick_spin(array, x_coord, y_coord, T):
    '''Part 4: chooses to flip a position or keep it in original state'''
    J = energy(array)
    array[x_coord][y_coord] = -1 * array[x_coord][y_coord]
    J_flip = energy(array)
    if J > J_flip:
        return array
    else:
        E = J - J_flip
        a = random.random()
        b = array_plot.boltzmann(E,T)
        if a > b:
            return array
        else:
            array[x_coord][y_coord] = -1 * array[x_coord][y_coord]
            return array
          
    
