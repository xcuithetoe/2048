import random

def zeros_left(grid, row, start_column):
    zeros = 0

    for column in range(start_column, 4):
        if grid[row][column] != 0:
            break
        zeros += 1
    return zeros
'''
def zeros_right(grid, row, start_column):
    zeros = 0

    for column in range(3, (start_column - 1), -1):
        if grid[row][column] != 0:
            break

        zeros += 1
    return zeros
'''
def zeros_up(grid, column, start_row):
    zeros = 0

    for row in range(start_row, 4):
        if grid[row][column] != 0:
            break
        zeros += 1
    return zeros
def pretty_print(grid):
    '''
    This prints the 2048 logic grid in terminal
    This is an example print:
    
    [0, 0, 2, 4]
    [2, 2, 2, 4]
    [2048, 0, 8]
    [16, 32, 64, 128]
    '''
    for i in range(4):
        print(grid[i])
    print('')
    

def create_grid(grid):
    '''
    creates a 4 x 4 grid
    '''
    for i in range(4):
        grid.append([0, 0, 0, 0])
    return grid

def add_one(grid):
    '''
    adds a '2' to a random place in the grid, if the grid number is 0(empty)
    '''
    not_in = True
    random_row = random.randint(0, 3)
    random_column = random.randint(0, 3)
    while not_in:
        if grid[random_row][random_column] == 0:
            grid[random_row][random_column] = 2
            not_in = False
    return grid

def reverse_horizontally(grid):
    new_mat =[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(grid[i][3 - j])
    return new_mat
def reverse_vertically(grid):
    new_mat =[]
    for j in range(4):
        new_mat.append([])
        for i in range(4):
            new_mat[i].append(grid[3 - i][j])
    return new_mat

def up(grid):
    '''
    moves everything left
    The code basically checks every number in every row from left to right, and if that number is 0(empty), then everything shifts one space to the left
    Then, the code checks for any repition. It checks every two number, and if the two numbers are the same, them 
    '''
    wa = 0
    for column in range(4):
        for row in range(4):
            num_zeros = zeros_up(grid, column, row)
            
            if num_zeros != 0:
                try:
                    grid[row][column] = grid[row + num_zeros][column]
                    grid[row + num_zeros][column] = 0
                except:
                    wa = 1
            
    return grid

def down(grid):
    grid = reverse_vertically(grid)
    grid = left(grid)
    grid = reverse_vertically(grid)

def right(grid):
    grid = reverse_horizontally(grid)
    grid = left(grid)
    grid = reverse_horizontally(grid)

    return grid

def left(grid):
    '''
    moves everything left
    The code basically checks every number in every row from left to right, and if that number is 0(empty), then everything shifts one space to the left
    Then, the code checks for any repition. It checks every two number, and if the two numbers are the same, them 
    '''
    wa = 0
    for row in range(4):
        for column in range(4):
            num_zeros = zeros_left(grid, row, column)
            
            if num_zeros != 0:
                try:
                    grid[row][column] = grid[row][column + num_zeros]
                    grid[row][column + num_zeros] = 0
                except:
                    wa = 1
            
    return grid