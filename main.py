import logic 

grid = []
logic.create_grid(grid)


grid[0][1] = 2
grid[0][3] = 8


logic.pretty_print(grid)

grid = logic.down(grid)

logic.pretty_print(grid)