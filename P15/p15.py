
def extract_digits(lines):
    digits = []
    # digits are the last part of the line after the '|'.
    # There should be 4 digits.
    for line in lines:
        digits.append(line.split('|')[1].strip())
    return digits

def count_1478_digits(four_digits):
    digits = four_digits.split()
    sum = 0
    # The number of sigments in digits 1,4,7 & 8 are unique
    # They have 2,4,3 and 7 segments respectively.
    for digit in digits:
        if len(digit) in [2,3,4,7]:
            sum += 1
    return sum

file1 = open('input.txt', 'r')
Lines = file1.readlines()

# Get a list of 4 digit displays
digits_list = extract_digits(Lines)
# Count the occurances of 1,4,7 & 8 digits in those displays.
sum = 0
for digit_display in digits_list:
    sum += count_1478_digits(digit_display)
print(sum)

