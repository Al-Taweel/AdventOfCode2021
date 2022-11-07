file1 = open('input.txt', 'r')

Lines = file1.readlines()
previous_line = -1
count = 0
for line in Lines:
    if previous_line != -1 and int(line) > previous_line:
        count +=1
    previous_line = int(line)

print (count)
