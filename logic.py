import random

def Is_Full(grid):
    fullnum = 0
    for row in range(4):
        for column in range(4):
            if grid[row][column] != 0:
                fullnum += 1
    
    isfull = False
    if fullnum == 16:
        isfull = True
    return isfull


def find_nums(grid):
    '''
    item0: 0
    item1: 2
    item2: 4
    item3: 8
    item4: 16
    item5: 32
    item6: 64
    item7: 128
    item8: 256
    item9: 512
    item10: 1024
    item11: 2048
    '''
    items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for row in range(4):
        for column in range(4):
            if grid[row][column] == 0:
                item[0] += 1
            if grid[row][column] == 2:
                item[1] += 1
            if grid[row][column] == 4:
                item[2] += 1
            if grid[row][column] == 8:
                item[3] += 1
            if grid[row][column] == 16:
                item[4] += 1            
            if grid[row][column] == 32:
                item[5] += 1      
            if grid[row][column] == 64:
                item[6] += 1            
            if grid[row][column] == 128:
                item[7] += 1            
            if grid[row][column] == 256:
                item[8] += 1 
            if grid[row][column] == 512:
                item[9] += 1
            if grid[row][column] == 1024:
                item[10] += 1
            if grid[row][column] == 2048:
                item[11] += 1 
    return items                                         

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
    return grid
    

def create_grid(grid):
    '''
    creates a 4 x 4 grid
    '''
    for i in range(4):
        grid.append([0, 0, 0, 0])
    return grid

def add_twos(grid, num):

    if Is_Full(grid):
        return None

    '''
    adds a '2' to a random place in the grid, if the grid number is 0(empty)
    '''
    for i in range(num):
        not_in = True

        while not_in:
            random_row = random.randint(0, 3)
            random_column = random.randint(0, 3)            
            
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
    new_mat =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        #new_mat.append([])
        for i in range(4):
            new_mat[i][j] = grid[3 - i][j]

    return new_mat
def up(grid):
    '''
    moves everything up
    The code basically checks every number in every row from left to right, and if that number is 0(empty), then everything shifts one space to the left
    Then, the code checks for any repition. It checks every two number, and if the two numbers are the same, them 
    '''
    for i in range(4):
        grid = goup(grid)
        grid = mergeup(grid)
        grid = goup(grid)
     #grid = goleft(grid)

            
    return grid
def goup(grid):
    '''
    moves everything up
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
    grid = up(grid)
    grid = reverse_vertically(grid)

    return grid

def right(grid):
    grid = reverse_horizontally(grid)
    grid = goleft(grid)
    grid = reverse_horizontally(grid)

    return grid

def left(grid):
    '''
    moves everything left
    The code basically checks every number in every row from left to right, and if that number is 0(empty), then everything shifts one space to the left
    Then, the code checks for any repition. It checks every two number, and if the two numbers are the same, them 
    '''
    for i in range(4):
        grid = goleft(grid)
        grid = merge(grid)
        grid = goleft(grid)


    return grid
def goleft(grid):
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
def merge(mat):

      
    for i in range(4):
        for j in range(3):
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):

                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
  
    return mat
def mergeup(mat):

      
    for j in range(4):
        for i in range(3):
            if(mat[i][j] == mat[i + 1][j] and mat[i][j] != 0):

                mat[i][j] = mat[i][j] * 2
                mat[i + 1][j] = 0


    return mat