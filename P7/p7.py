# Reads bingo boards into a 3D list 
def read_bingo_boards(lines):
    n = 0
    board = 0
    row = 0
    bingo_boards = []
    bingo_boards.append([])

    for line in lines:
        if line.strip() == '':
            continue
        bingo_boards[board].append(line.split())
        #n += 1
        row += 1
        if row == 5: # one board is fully read.
            bingo_boards.append([])
            row = 0
            board += 1
            #n += 1   # Skip the spacer line between boards.

    bingo_boards.pop()  #remove last entry because it's empty.
    return bingo_boards

# Marks a drawn number in all boards.
# When an entry is found, it is marked with a negative sign.  
def mark_number_in_boards(n,boards):
    for board in boards:
        for row in board:
            for number in range(len(row)):
                if row[number] == n:
                    row[number] = str(int(row[number])*-1)

# Checks all boards for a winner.
# returns the winning board if any else an empty list
def check_winning_board(boards):
    for board in boards:
        #check rows
        for row in board:
            bingo = True
            for number in row:
                if int(number) >= 0:
                    bingo = False
                    break
            if bingo:
                return board
        # check columns
        for column in range(5):
            bingo = True
            for row in range(5):
                if int(board[row][column]) >= 0:
                    bingo = False
                    break
            if bingo:
                return board
    return []    

file1 = open('input.txt', 'r')
Lines = file1.readlines()

#first line has the randomly drawn numbers for the bingo
drawn_numbers = Lines.pop(0).split(',')
bingo_boards = read_bingo_boards(Lines)

for number in drawn_numbers:
    mark_number_in_boards(number, bingo_boards)
    board = check_winning_board(bingo_boards)
    if board != []:
        sum = 0
        # add all unmarked numbers
        for row in board:
            for num in row:
                x = int(num)
                if x > 0:
                    sum += x
        print(sum * int(number))
        break


