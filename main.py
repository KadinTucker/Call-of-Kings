import worldDisplay
import worldGen
import pygame
from pygame.locals import *
import sys

worldsize = 200
world = worldGen.generateWorld(worldsize)

worldDisplay.layers['grid'] = worldDisplay.generateGridLayer(world)
worldDisplay.layers['terrain'] = worldDisplay.generateTerrainLayer(world)

display = pygame.display.set_mode((1250, 750))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            worldDisplay.window, worldDisplay.layers = worldDisplay.displayEvent(event, worldDisplay.window, worldDisplay.layers, worldsize)
        worldDisplay.display(worldDisplay.layers, display)

if __name__ == '__main__':
    main()
