import array_plot

def spin_periodic(array, x_coord, y_coord):
    '''Part 2: return spin in a cell, wrapping around if out of bounds.'''
    (side_x, side_y) = array.shape
    return array[x_coord % side_x][y_coord % side_y]
