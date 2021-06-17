
import pygame

class block(pygame.sprite.Sprite):
    def __init__(self, x, y, typeblock):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(str(typeblock) + '_block.png')
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def die(self):
        self.kill()

def block_pos(row, column, position='lowerright', outputmethod='two variables'):
    '''
    This is a simple calculator for calculating rectangular(aka cartesian) coordinates of any block, as long as you give the item number of the grid. 
    You can choose which point on the block would be the position calculated. The default is the 'lowerright' of the block, but you can also choose 'center', 'topleft', 'lowerleft', or 'topright'.

    You can choose three output methods. The first method, which is also the default method, is through two variables(eg 125, 125). The second is 'list', which would return something like [125, 125]. The third and final one is a  
    =======================================================
    Example use:

    grid = [[0, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #The number 'two' is on row 1 column 1(in python terms)

    block_pos(1, 1, 'center')

    ======================================================
    The example output would show:

    187, 187

    '''
    realx = (row + 1)*125
    realy = (column + 1)*125

    if position == 'center':
        realx -= (125/2)
        realy -= (125/2)
    elif position == 'topleft':
        realx -= 125
        realy -= 125
    elif position == 'lowerleft':
        realx += 125
    elif position == 'topright':
        realy -= 125
    elif position == 'lowerright':
        pass
      
    if outputmethod == 'list':
        return [realx, realy]
    elif outputmethod == 'tuple':
        return (realx, realy)
    else:
        return realx, realy









        