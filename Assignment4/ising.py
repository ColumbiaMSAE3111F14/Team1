import array_plot

def spin_periodic(array, x_coord, y_coord):
    '''Part 2: return spin in a cell, wrapping around if out of bounds.'''
    side = array.shape[0]
    return array[x_coord % size][y_coord % size]
