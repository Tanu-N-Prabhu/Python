# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        # node of nodes
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the directed graph
        for (src, dest) in edges:
            # allocate node in adjacency list from src to dest
            # node -> node or null
            self.adjList[src].append(dest)
 
 
# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adjList[src]:
            print(f'({src} —> {dest}) ', end='')
        print()
 
 
if __name__ == '__main__':
 
    # Input: Edges in a directed graph
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
 
    # No. of vertices (labelled from 0 to 5)
    n = 6
 
    # construct a graph from a given list of edges
    graph = Graph(edges, n)
 
    # print adjacency list representation of the graph
    printGraph(graph)