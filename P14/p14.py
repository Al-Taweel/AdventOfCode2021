def fill_crab_positions(positions,crabs):
    for crab in crabs:
        positions[crab] += 1

def calc_fuel_costs(positions):
    fuel_costs = [0 for n in positions]
    for i in range(len(fuel_costs)):
        for position in range(len(positions)):
            # Costs follow the triangular numbers formula (n(n+1))/2 
            # The cost is the number of crabs to move * triangular number.
            n = abs(position - i) 
            fuel_costs[i] +=  int((n*(n+1))/2) * positions[position]

    return fuel_costs

file1 = open('input.txt', 'r')
Lines = file1.readlines()

all_crab_positions = [int(n) for n in str(Lines[0]).split(',')]

highest_position = max(all_crab_positions)

crab_positions = [0 for n in range(highest_position+1)]
fill_crab_positions(crab_positions,all_crab_positions)

fuel_costs = calc_fuel_costs(crab_positions)

print(min(fuel_costs))