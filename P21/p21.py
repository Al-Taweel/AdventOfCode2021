class Octopus:
    def __init__(self, energy_level, flashed):
        self.energy_level = energy_level
        self.flashed = flashed

num_of_steps = 100
grid_size = 10
# A list to keep the energy levels of all octopuses
energy_levels = []

def fill_energy_levels(lines):
    for line in Lines:
        line = line.strip()
        energy_levels.append([Octopus(int(a),False) for a in [*line]])

def increase_adjacent_energy_levels(x,y):
    if x < 1:
        min_x = 0
    else:
        min_x = x-1
    if x > grid_size - 2:
        max_x = grid_size - 1
    else:
        max_x = x+1
    if y < 1:
        min_y = 0
    else:
        min_y = y-1
    if y > grid_size - 2:
        max_y = grid_size - 1
    else:
        max_y = y+1       

    for adjacent_y in range(min_y, max_y+1):    
        for adjacent_x in range(min_x, max_x+1):
            energy_levels[adjacent_y][adjacent_x].energy_level += 1

# Increment the energy level of all octopuses by 1
def increase_energy_levels():
    for y in energy_levels:
        for x in y:
            x.energy_level += 1

def check_flashing():
    count = 0
    for y in range(len(energy_levels)):
        for x in range(len(energy_levels[0])):
            if energy_levels[y][x].energy_level >9 and not energy_levels[y][x].flashed:
                energy_levels[y][x].flashed = True
                increase_adjacent_energy_levels(x,y)
                count += 1

    return count
  
def reset_flashes():
    count = 0
    for y in energy_levels:
        for x in y:
            if x.flashed == True:
                x.energy_level = 0
                x.flashed = False
                count += 1

    return count


file1 = open('input.txt', 'r')
Lines = file1.readlines()

fill_energy_levels(Lines)
total_flashes = 0
for step_no in range(num_of_steps):
    increase_energy_levels()
    while check_flashing():
        pass
    total_flashes += reset_flashes()

print(total_flashes)
