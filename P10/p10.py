grid_size = 1000
# convert lines into integer line co-ordinates
def extract_lines(Lines):
    extracted_lines= []
    for line in Lines:
        line = line.strip()
        temp = line.split(' -> ')
        x1,y1 = temp[0].split(',')
        x2,y2 = temp[1].split(',')
        #if x1 == x2 or y1 == y2:
        extracted_lines.append(((int(x1),int(y1)),(int(x2),int(y2))))
    return extracted_lines

def generate_grid():
    grid = []
    for i in range(grid_size):
        grid.append([0 for a in range(grid_size)])
    return grid

def fill_grid(grid, lines):
    for line in lines:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if x1 == x2:
            # generate enough x values for the number of y values.
            x = [x1 for n in range(abs(y2 - y1)+1)]
        elif x1 > x2:
            x = [n for n in range(x1,x2-1,-1)]
        else:
            x = [n for n in range(x1,x2+1,1)]
        if y1 == y2:
            # generate enough y values for the number of x values.
            y = [y1 for n in range(abs(x2 - x1)+1)]
        elif y1 > y2:
            y = [n for n in range(y1,y2-1,-1)]
        else:
            y = [n for n in range(y1,y2+1,1)]
        n = 0
        for i in range(len(x)):
            grid[x[i]][y[i]] += 1
        n = 1
    return grid

def check_overlap(grid):
    sum = 0
    for x in grid:
        for y in x:
            if y > 1:
                sum += 1
    return sum

file1 = open('input.txt', 'r')
Lines = file1.readlines()

vent_lines = extract_lines(Lines)
# Get an empty grid to plot the lines on.
grid = generate_grid()
# Plot the ines on the grid.
grid = fill_grid(grid, vent_lines)
overlap = check_overlap(grid)
print(overlap)