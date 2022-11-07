file1 = open('input.txt', 'r')

Lines = file1.readlines()
no_of_lines = len(Lines)
count = []
no_of_bits = 0

for line in Lines:
    no_of_bits = len(line)-1
    for bit in range(no_of_bits):
        if len(count) == bit:
            count.append(0)
        count[bit] += int(line[bit])

gamma = ['1' if a>no_of_lines/2 else '0' for a in count]
epsilon = ['1' if a=='0' else '0' for a in gamma]

print(gamma)
print(epsilon)

print (int(''.join(gamma),2)*int(''.join(epsilon),2))

