file1 = open('input.txt', 'r')

Lines = file1.readlines()
count = 0
no_of_meas = int(len(Lines))
measurements = [int(x) for x in Lines]
previous_meas_window = measurements[0] + measurements[1] + measurements[2]
for w in range(no_of_meas-2):
    current_meas_window = measurements[w] + measurements[w+1] + measurements[w+2]
    if current_meas_window > previous_meas_window:
        count += 1
    previous_meas_window = current_meas_window

print (count)
