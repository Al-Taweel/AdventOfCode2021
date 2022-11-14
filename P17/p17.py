# separate the input into a list of digits
def build_heightmap(Lines):
    heightmap =[]
    for line in Lines:
        line = line.strip()
        heightmap.append([*line])
    return heightmap

# Find low points by comparing adajacent points
def find_low_points(heightmap):
    max_y = len(heightmap)
    low_points = []
    for y in range(max_y):
        max_x = len(heightmap[y])
        for x in range(max_x):
            low_point = True
            point = heightmap[y][x]
            if x > 0: # check point to the left
                if heightmap[y][x-1] <= point:
                    low_point = False
            if x < max_x - 1: #check point to the right
                if heightmap[y][x+1] <= point:
                    low_point = False
            if y > 0: # check point to the top
                if heightmap[y-1][x] <= point:
                    low_point = False
            if y < max_y - 1: #check point to the bottom
                if heightmap[y+1][x] <= point:
                    low_point = False
            if low_point:
                low_points.append(int(heightmap[y][x]))

    return low_points

file1 = open('input.txt', 'r')
Lines = file1.readlines()

lowpoint_sum = 0
heightmap = build_heightmap(Lines)
low_points = find_low_points(heightmap)
# The risk level of a low point is 1 plus its height.
lowpoint_sum = sum(low_points)+len(low_points)

print(lowpoint_sum)