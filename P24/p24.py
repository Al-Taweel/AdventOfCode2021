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
# flag is used to indicate that one small cave has
# been visited twice, so no more small caves are allowed.
# flag_was_set is used to reset the flag (but only at the same
# level in the tree where it was set.)
def find_all_paths(path_so_far, new_path, connections, flag):
    flag_was_set = False
    for path in connections[new_path]:
        if path == 'start':
            continue
        if path.islower() and path in path_so_far:
            if flag:
                continue
            else:
                flag = True
                flag_was_set = True
        if path == 'end':
            path_so_far.append(path)
            all_paths.append(path_so_far[:])
            path_so_far.pop()
        else:
            path_so_far.append(path)
            find_all_paths(path_so_far, path, connections, flag)
            path_so_far.pop()
            if flag_was_set:
                flag = False 
    return

file1 = open('input.txt', 'r')
Lines = file1.readlines()

connections = find_all_connections(Lines)
find_all_paths(['start'], 'start', connections, False)
print(len(all_paths))
