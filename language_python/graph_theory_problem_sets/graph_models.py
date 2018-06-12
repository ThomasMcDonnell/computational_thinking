
class Node:
    """ Nodes represent points where roads end or meet """

    def __init__(self, name):
        self.name = name    # assumed name is a string 

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    """ Edges are connections between points/nodes """

    def __init__(self, src, dest):
        self.src = src  # Node
        self.dest = dest    # Node

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return (self.src.get_name() +
               '==>' + self.dest.get_name())


"""
Digraph: Nodes are represented as keys in a dictionary and Edges are
represented by destinations as values in a list associated with a source key.
"""
class Digraph:
    """" Edges is a dict mapping, each node is the key to a list of its
    destinations """

    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node') # Node already a key in dict
        self.edges[node] = []   # set Node as key to an empty list 

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()

        # Check both src & dest are in the dict
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node Not In Graph')
        self.edges[src].append(dest) # use src as key and place dest in list

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for node in self.edges:
            if node.get_name() == name:
                return node
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = (result + '(' + src.get_name() + ')' +
                          '==>>==>>==>>' + '('
                          + dest.get_name() + ')' + '\n')
        return result[:-1]  # omit final new line  


"""
Graph: Inherites from Digraph and since Graph has no sense of direction to its
edges i.e you can go each way, we extend this sort of functionality by adding
an edge each way. (src) ==>>==>> (dest)
                       <<==<<==
"""
class Graph(Digraph):

    def add_edge(self, edge):
        Digraph.add_edge(self, edge) # add first edge
        rev = Edge(edge.get_destination(), edge.get_source()) # reverse
        Digraph.add_edge(self, rev) # add reverse edge


if __name__ == '__main__':
    main()


