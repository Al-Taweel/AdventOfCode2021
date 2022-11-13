# digits are the last part of the line after the '|'.
# There should be 4 digits.
def extract_digits(line):
    digits = line.split('|')[1].strip().split()
    return digits

# inputs: d1, d7 are strings with the codes for digits 1 and 7
# returns: the code for the 'top' segment
def find_code_for_top_segment(d1,d7):
    for d in d7:
        if d in d1:
            continue
        return d

# inputs: d1, d4 are strings with the codes for digits 1 and 4
# returns: the code for the 'left_top & middle' segments
def find_code_for_ltm_segments(d1,d4):
    ltm_code =[]
    for d in d4:
        if d not in d1:
            ltm_code.append(d)
    
    return ltm_code

# Function gets 1 line containing the codes for digits 0-9
# It deduces the digits' codes from those.
# It returns a list of digit codes
def get_digits_codes(line):
    # identify digits 1,4,7 & 8
    digits =[[],[],[],[],[],[],[],[],[],[]]
    codes_part = line.split('|')[0]
    codes = codes_part.split()
    for code in codes:
        length = len(code)
        if length == 2:  # We found '1'
            digits[1] = ''.join(sorted(code))
        elif length == 3: # We found '7'
            digits[7] = ''.join(sorted(code))
        elif length == 4: # We found '4'
            digits[4] = ''.join(sorted(code))
        elif length == 7: # We found '8'
            digits[8] = ''.join(sorted(code))

    # find 'top' segment (which is in 7 but not in 1)
    top = find_code_for_top_segment(digits[1],digits[7])
    righttop_rightbottom = [*digits[1]]
    lefttop_middle = find_code_for_ltm_segments(digits[1],digits[4])
    for code in codes:
        code = ''.join(sorted(code)) 
        length = len(code)
        if length == 5:
            if set(righttop_rightbottom).issubset(code):  # we fond digit '3'
                digits[3] = code
            elif set(lefttop_middle).issubset(code): # we found digit '5'
                digits[5] = code
            else:  # we found digit 2
                digits[2] = code
        if length == 6:
            if set(lefttop_middle).issubset([*code]) and set(righttop_rightbottom).issubset([*code]) : # we found digit '9'
                digits[9] = code
            elif set(righttop_rightbottom).issubset([*code]): # we found digit '0'
                digits[0] = code
            else:  # we found digit'6'
                digits[6] = code
    return digits

# Compare digits in 'digits_list' to values in 'codes'
# to get a total value of the 4 digit display.  
def get_digit_display_value(codes,digits_list):
    digits = ['0','0','0','0']
    for code in range(len(codes)):
        for digit in range(len(digits_list)):
            sorted_digit = ''.join(sorted(digits_list[digit]))
            if  sorted_digit == codes[code]:
                digits[digit] = str(code)
    return int(''.join(digits))


file1 = open('input.txt', 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    digits_codes = get_digits_codes(line)
    # Get a list of 4 digit display at the end of the line
    digits_list = extract_digits(line)
    value = get_digit_display_value(digits_codes,digits_list)
    sum += value
    
print(sum)