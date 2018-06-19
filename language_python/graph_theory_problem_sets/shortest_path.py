from graph_models import *
from depth_first_search import *


def build_city_graph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):           # Create 7 nodes
        g.add_node(Node(name))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g


def test_shortest_path(source, destination):
    g = build_city_graph(Digraph)
    shortest = shortestPath(g, g.get_node(source), g.get_node(destination),
                             _print=True)
    if shortest != None:
        print(f'Shortest path from {source} to {destination} is ',
             print_path(shortest))
    else:
        print(f'There is no path from {source} to {destination}')


if __name__ == '__main__':
    #test_shortest_path('Chicago', 'Boston')
    test_shortest_path('Boston', 'Phoenix')


