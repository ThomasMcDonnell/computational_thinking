"""
The idea here is to go as deep as possible until    a) we find a solution
                                                    b) we run out of edges
Once one of the two are true we backtrack to the next node and repeat
recursively. Once all posibilities have been explored we return the optimal
solution.
"""


def print_path(path): # function to print current path assuming path = [Nodes]
    result = ''
    for i in range(len(path)):
        result = result + '(' + str(path[i]) + ')'
        if i != len(path) - 1:
            result =  result + '==>'
    return result


def DFS(graph, start, end, path, shortest, _print = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if _print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                new_path = DFS(graph, node, end, path, shortest,
                              _print)
                if new_path != None:
                    shortest = new_path
        elif _print:
            print(f'Already visited {node}')
    return shortest


def shortestPath(graph, start, end, _print = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, [], None, _print)

if __name__ == '__main__':
    main()
