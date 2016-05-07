#Defining Terrain types

from datastructure import terrain
from resource import *
import pygame

class grassland(terrain):
    def __init__(self):
        super(grassland, self).__init__()
        self.resources = [wool(), hide(), grain(), grapes()]
        self.image = pygame.image.load('grass.png')
        self.type = 'grassland'

class plains(terrain):
    def __init__(self):
        super(plains, self).__init__()
        self.resources = [flax(), hide(), grain(), hay()]
        self.image = pygame.image.load('plains.png')
        self.type = 'plains'
        
class tundra(terrain):
    def __init__(self):
        super(tundra, self).__init__()
        self.resources = [fur(), dye(), grain(), herbs()]
        self.image = pygame.image.load('tundra.png')
        self.type = 'tundra'

class desert(terrain):
    def __init__(self):
        super(desert, self).__init__()
        self.resources = [flax(), clay(), vegetable(), salt()]
        self.image = pygame.image.load('desert.png')
        self.type = 'desert'

class lake(terrain):
    def __init__(self):
        super(lake, self).__init__()
        self.resources = [herbs(), water(), meat(), salt()]
        self.image = pygame.image.load('lake.png')
        self.type = 'lake'

class forest(terrain):
    def __init__(self):
        super(forest, self).__init__()
        self.resources = [silk(), wood(), meat(), fur()]
        self.image = pygame.image.load('forest.png')
        self.type = 'forest'

class jungle(terrain):
    def __init__(self):
        super(jungle, self).__init__()
        self.resources = [silk(), water(), wood(), vegetable()]
        self.image = pygame.image.load('jungle.png')
        self.type = 'jungle'

class mountain(terrain):
    def __init__(self):
        super(mountain, self).__init__()
        self.resources = [dye(), metal(), vegetable(), clay()]
        self.image = pygame.image.load('mountain.png')
        self.type = 'mountain'

class hill(terrain):
    def __init__(self):
        super(hill, self).__init__()
        self.resources = [wool(), hide(), meat(), olives()]
        self.image = pygame.image.load('hill.png')
        self.type = 'hill'

terrainDict = {0 : grassland, 1 : plains, 2 : tundra, 3 : desert, 4 : lake, 5 : forest, 6 : jungle, 7 : mountain, 8 : hill}

