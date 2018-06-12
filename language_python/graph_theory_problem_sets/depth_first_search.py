"""
The idea here is to go as deep as possible until    a) we find a solution
                                                    b) we run out of edges
Once one of the two are true we backtrack to the next node and repeat
recursively. Once all posibilities have been explored we return the optimal
solution.
"""

def depth_first_search(graph, start, end, path, shortest, _print=False):
    path = path + [start]
    if _print:
        print('Current DFS Path: ', print_path(path))
    if start == end:
        return path

    for node in graph.childern_of(start):
        if node not in path:    # Avoid constant cycles
            if shortest == None or len(path) < len(shortest):
                new_path = depth_first_search(graph, node, end, path, shortest,
                                              _print)
                if new_path != None:
                    shortest = new_path
        elif _print:
            print('Already visited', node)

    return shortest

