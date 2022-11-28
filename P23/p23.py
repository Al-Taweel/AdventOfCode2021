all_paths = []

# Convert input into a dictionary.
# key: a point in the tree.
# value: a list of points connected to it.
def find_all_connections(Lines):
    connections = {}
    for con in Lines:
        con = con.strip().split('-')
        first = con[0]
        second = con[1]
        if first in connections:
            connections[first].append(second)
        else:
            connections[first] = [second]
        if second in connections:
            connections[second].append(first)
        else:
            connections[second] = [first]
    return connections

# Try all possible paths recursively
def find_all_paths(path_so_far, new_path, connections):
    for path in connections[new_path]:
        if path.islower() and path in path_so_far:
            continue 
        if path == 'end':
            path_so_far.append(path)
            all_paths.append(path_so_far[:])
            path_so_far.pop()
        else:
            path_so_far.append(path)
            find_all_paths(path_so_far, path, connections)
            path_so_far.pop()     
    return

file1 = open('input.txt', 'r')
Lines = file1.readlines()

connections = find_all_connections(Lines)
find_all_paths(['start'], 'start', connections)
print(len(all_paths))
