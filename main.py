import logic 
import pygame
import sys
import os
import board
import time


grid = []
grid = logic.create_grid(grid)
grid = logic.add_twos(grid, 2)
fps = 30

'''
grid[0][0] = 2
grid[1][0] = 2
grid[3][0] = 2
grid[2][0] = 2


'''

worldx = 500
worldy = 500

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

world = pygame.display.set_mode([worldx, worldy])

#--------------------------------------

backdrop = pygame.image.load('2048game_background.png')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

block_list = pygame.sprite.Group()
logic.pretty_print(grid)
#-----------------------------------------

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quit by exiting')
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            block_list.empty()
            #logic.pretty_print(grid)

            if event.key == ord('a') or event.key == pygame.K_LEFT:
                grid = logic.left(grid)
                #block_list.empty()
            if event.key == ord('d') or event.key == pygame.K_RIGHT:
                grid = logic.right(grid)
                #block_list.empty()
            if event.key == ord('w') or event.key == pygame.K_UP: 
                grid = logic.up(grid)
                #block_list.empty()
            if event.key == ord('s') or event.key == pygame.K_DOWN:
                grid = logic.down(grid)
                #block_list.empty()
            grid = logic.add_twos(grid, 1)
            logic.pretty_print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column] != 0:
                blocknum = grid[row][column]
                cors = board.block_pos(row, column, position='topright', outputmethod='list')
                new_block = board.block(cors[0], cors[1], grid[row][column])
                block_list.add(new_block)


    world.blit(backdrop, backdropbox)
    new_block.update()

    block_list.draw(world)
    

    pygame.display.flip()
    clock.tick(fps)