file1 = open('input.txt', 'r')

Lines = file1.readlines()
horizontal = 0
depth = 0
aim = 0
for line in Lines:
    action = line.split()
    if action[0] == 'forward':
        horizontal += int(action[1])
        depth += aim*int(action[1])

    elif action[0] == 'down':
        aim += int(action[1])
    else:
        aim -= int(action[1])

print (horizontal*depth)
