# Takes a list of binary strings and
# finds what's the most common bit value '0' or '1'
# at bit position n and returns a list of numbers with 
# that bit.
def most_common_value(binary_numbers,n):
    nos_with_zero_bit = [x for x in binary_numbers if x[n]=='0']
    nos_with_one_bit = [x for x in binary_numbers if x[n]=='1']
    if len(nos_with_zero_bit) > len(nos_with_one_bit):
        return nos_with_zero_bit
    else:
        return nos_with_one_bit
    
# Takes a list of binary strings and
# finds what's the least common bit value '0' or '1'
# at bit position n and returns a list of numbers with 
# that bit.
def least_common_value(binary_numbers,n):
    nos_with_zero_bit = [x for x in binary_numbers if x[n]=='0']
    nos_with_one_bit = [x for x in binary_numbers if x[n]=='1']
    if len(nos_with_one_bit) < len(nos_with_zero_bit):
        return nos_with_one_bit
    else:
        return nos_with_zero_bit


file1 = open('input.txt', 'r')
Lines = file1.readlines()

oxygen_generator_rating = Lines
n = -1
# Filter values for oxygen generator rating
while len(oxygen_generator_rating)!=1:
    n += 1
    oxygen_generator_rating = most_common_value(oxygen_generator_rating,n)

CO2_scrubber_rating = Lines
n = -1
# Filter values for CO2 scrubber rating
while len(CO2_scrubber_rating)!=1:
    n += 1
    CO2_scrubber_rating = least_common_value(CO2_scrubber_rating,n)

int_oxygen_generator_rating = int(''.join(oxygen_generator_rating),2)
int_CO2_scrubber_rating = int(''.join(CO2_scrubber_rating),2)
print (int_oxygen_generator_rating * int_CO2_scrubber_rating)

