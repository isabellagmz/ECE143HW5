# Isabella Gomez A15305555
# ECE143 HW5

import numpy as np
import random

def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    This function takes in a size for a canvas and a direction for a slash that
    will be randomly generated. The slash must have at least 2 non-zero pixels
    that are contiguous.

    :param m: number of rows of the image
    :param n: number of columns of the image
    :param direction: can be forward or back, direction of slash
    :return: an array that will show a slash in a given direction
    '''

    # check n and m are ints
    assert type(m) == int and type(n) == int

    # check that direction is back or forward
    assert type(direction) == str
    assert (direction == 'back' or direction == 'forward')

    # create the array and populate with zeros
    ran_gen_array = np.zeros((m,n))

    # get a random number between 0 and 4 when back
    if direction == 'back':
        random_column = random.randint(0, n-2)
        random_start_row = random.randint(0, m-2)
        random_end_row = random.randint(random_start_row+1, m-1)
        # put a 1 where the random column was generated
        for row in range(n):
            ran_gen_array[random_start_row][random_column] = 1
            # move the ones from row_start to row_end
            if random_column != n-1 and random_start_row != random_end_row:
                random_column = random_column + 1
                random_start_row = random_start_row + 1
            else:
                break

    # get a random number between 1 and 5 when direction is forward
    elif direction == 'forward':
        random_column = random.randint(1, n-1)
        random_start_row = random.randint(0, m-2)
        random_end_row = random.randint(random_start_row + 1, m-1)
        # put a 1 where the random number was generated
        for row in range(n):
            ran_gen_array[random_start_row][random_column] = 1
            if random_column != 0 and random_start_row != random_end_row:
                random_column = random_column - 1
                random_start_row = random_start_row + 1
            else:
                break

    return ran_gen_array
