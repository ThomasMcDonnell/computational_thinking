
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

class Digraph:

    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node Not In Graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = (result + '(' + src.get_name() + ')' +
                          '==>>==>>==>>' + '('
                          + dest.get_name() + ')' + '\n')
        return result[:-1]  # omit final new line  


class Graph(Digraph):

    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


if __name__ == '__main__':
    main()


