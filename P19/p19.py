error_values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

expected_close = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

def check_corrupted(line,open_chunks,expected_chunck_close):
    error_value = 0
    openings = ['(','[','{','<']
    while line != [] and error_value == 0:        
        c = line.pop(0)
        if c in openings:  # Beginning of a chunk
            open_chunks.append(c)
            error_value += check_corrupted(line,open_chunks,expected_close[c])
        else:   # it's a chunk closing char 
            if c == expected_chunck_close:
                open_chunks.pop()
                if open_chunks:
                    expected_chunck_close = expected_close[open_chunks[len(open_chunks)-1]]
                else:
                    expected_chunck_close = ''
            else: # mismatch in closing char
                error_value = error_values[c]
    return error_value

file1 = open('input.txt', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    line = line.strip()
    sum += check_corrupted([*line],[],'')

print(sum)