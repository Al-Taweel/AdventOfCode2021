# separate the input into a list of digits
def build_heightmap(Lines):
    heightmap =[]
    for line in Lines:
        line = line.strip()
        heightmap.append([*line])
    return heightmap

def add_basin(heightmap,x,y,max_x,max_y):
    if heightmap[y][x] in ['9','*']:
        return 0
    # Check the surrounding points for basin barrier (i.e. a '9' or a '*')
    sum = 1
    heightmap[y][x] = '*'
    if x < max_x-1:
        sum += add_basin(heightmap,x+1,y,max_x,max_y)
    if x > 0:
        sum += add_basin(heightmap,x-1,y,max_x,max_y)
    if y < max_y-1:
        sum += add_basin(heightmap,x,y+1,max_x,max_y)
    if y > 0:
        sum += add_basin(heightmap,x,y-1,max_x,max_y)
    
    return sum

def find_basins(heightmap):
    basins = []
    max_y = len(heightmap)
    for y in range(max_y):
        max_x = len(heightmap[y])
        for x in range(max_x):
            if heightmap[y][x] not in ['9','*']:
                basins.append(add_basin(heightmap,x,y,max_x,max_y))
    return basins

file1 = open('input.txt', 'r')
Lines = file1.readlines()

lowpoint_sum = 0
heightmap = build_heightmap(Lines)
basins = find_basins(heightmap)
# Find the product of the largest 3 basins
product = 1
for basin in range(3):
    max_basin = max(basins)
    product *= max_basin
    basins.remove(max_basin)
print(product)