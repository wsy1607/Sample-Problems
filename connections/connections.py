connections = [('a','b'),('a','c'),('b','c'),('c','d'),('a','d')]
all_i_connections = [c[0] for c in connections]
all_j_connections = [c[1] for c in connections]
output = []
for i in set(all_i_connections):
    for j in set(all_j_connections):
        if i == j:
            continue
        else:
            i_connections_left = [c[1] for c in connections if c[0] == i]
            i_connections_right = [c[0] for c in connections if c[1] == i]
            i_connections = i_connections_left  + i_connections_right
            j_connections_left = [c[1] for c in connections if c[0] == j]
            j_connections_right = [c[0] for c in connections if c[1] == j]
            j_connections = j_connections_left  + j_connections_right
            row = (i,j,len(set(i_connections) & set(j_connections)))
            output.append(row)

print(output)
