import logic 

grid = []
logic.create_grid(grid)
print(grid)

grid[0][1] = 2
grid[0][3] = 2

logic.left(grid)

logic.pretty_print(grid)