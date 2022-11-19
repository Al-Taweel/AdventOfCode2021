expected_close = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

closing_value = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def calc_completion_value(open_chunks):
    total = 0
    while open_chunks:
        total *= 5
        c = open_chunks.pop()
        expected_c = expected_close[c]
        total += closing_value[expected_c]

    return total

def get_open_chunks(line):
    openings = ['(','[','{','<']
    open_chunks = []
    expected_chunck_close = ''
    while line != []:
        c = line.pop(0)
        if c in openings:  # Beginning of a chunk
            open_chunks.append(c)
            expected_chunck_close = expected_close[c]
        else:   # it's a chunk closing char 
            if c == expected_chunck_close:
                open_chunks.pop()
                if open_chunks:
                    expected_chunck_close = expected_close[open_chunks[len(open_chunks)-1]]
                else:
                    expected_chunck_close = ''
                
            else: # Wrong chunck closing. Discard the line.
                return []
        
    return open_chunks

file1 = open('input.txt', 'r')
Lines = file1.readlines()

all_completion_values = []
for line in Lines:
    line = line.strip()
    open_chunks = get_open_chunks([*line])
    if open_chunks:
        completion_value = calc_completion_value(open_chunks)     
        all_completion_values.append(completion_value)
all_completion_values.sort()
middle_value = int(len(all_completion_values)/2)
print(all_completion_values[middle_value])