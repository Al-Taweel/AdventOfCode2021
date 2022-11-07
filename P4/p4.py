file1 = open('input.txt', 'r')

Lines = file1.readlines()
horizontal = 0
depth = 0
for line in Lines:
    action = line.split()
    if action[0] == 'forward':
        horizontal += int(action[1])
    elif action[0] == 'down':
        depth += int(action[1])
    else:
        depth -= int(action[1])

print (horizontal*depth)
