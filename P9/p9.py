grid_size = 1000

def extract_vertical_and_horizontal_lines(Lines):
    v_h_lines= []
    for line in Lines:
        line = line.strip()
        temp = line.split(' -> ')
        x1,y1 = temp[0].split(',')
        x2,y2 = temp[1].split(',')
        if x1 == x2 or y1 == y2:
            v_h_lines.append(((int(x1),int(y1)),(int(x2),int(y2))))
    return v_h_lines

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
            if y1 > y2:
                start = y2
                finish = y1 + 1
            else:
                start = y1
                finish = y2 + 1
            for y in range(start,finish):
                a = grid[x1][y]
                grid[x1][y] += 1
                b = grid[x1][y]
        else:
            if x1 > x2:
                start = x2
                finish = x1 + 1
            else:
                start = x1
                finish = x2 + 1
            for x in range(start,finish):
                a = grid[x][y1]
                grid[x][y1] += 1
                b = grid[x][y1]

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

# Lines has vertical, horizontal & diagonal lines
# We only need vertical & horizontal lines.
vent_lines_v_h = extract_vertical_and_horizontal_lines(Lines)
# Get an empty grid to plot the lines on.
grid = generate_grid()
# Plot the vertical & horizontal lines on the grid.
grid = fill_grid(grid, vent_lines_v_h)
overlap = check_overlap(grid)
print(overlap)