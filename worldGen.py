import random
import terrain

BIOME_SYMBOLS = '. ~ + * = # & ^ @ :'.split()

def zero_matrix(nrows, ncols):
    xop=[]
    for i in range(nrows):
        xop.append([0]*ncols)
    return xop
    
    
def pick_next_biome(current_biome, n_biomes, prob_same_type):
    if random.random()<prob_same_type:
        b = current_biome
    else:
        b = random.randint(0, n_biomes-1)
    return b
    

def generate_biome_map(n_biomes, nrows, ncols, correlation_factor):
    biome = zero_matrix(nrows, ncols)
    biome[0][0] = random.randint(0, n_biomes-1)
    for c in range(1, ncols):
        biome[0][c] = pick_next_biome(biome[0][c-1], n_biomes, correlation_factor)
    for r in range(1, nrows):
        biome[r][0] = pick_next_biome(biome[r-1][0], n_biomes, correlation_factor)
        for c in range(1, ncols):
            if random.randint(0,1)==1:
                b = biome[r][c-1]
            else:
                b = biome[r-1][c]
            biome[r][c] = pick_next_biome(b, n_biomes, correlation_factor)
            
    return biome

def translateMap(biome_map):
    for x in range(len(biome_map)):
        for y in range(len(biome_map[x])):
            biome_map[x][y] = terrain.terrainDict[biome_map[x][y]]()
    return biome_map
        

def generateWorld(worldsize):
    biome_map = generate_biome_map(9, worldsize, worldsize, 0.97)
    biome_map = translateMap(biome_map)
    return biome_map

