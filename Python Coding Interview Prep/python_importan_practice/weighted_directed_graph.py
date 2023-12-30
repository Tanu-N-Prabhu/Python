from queue import Queue


# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [None] * n
 
        # allocate memory for the adjacency list
        for i in range(n):
            self.adjList[i] = []
 
        # add edges to the directed graph
        for (src, dest, weight) in edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append((dest, weight))

    def childrenOf(self, node):
        return self.adjList[node]


    """
    def recursive_dfs(graph, source,path = []):
       if source not in path:
           path.append(source)
           if source not in graph:
               # leaf node, backtrack
               return path
           for neighbour in graph[source]:
               path = recursive_dfs(graph, neighbour, path)
       return path
    """
    def DFS(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.adjList[start]:
            if neighbour not in visited:
                result = self.DFS(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None 


    def BFS(self, start_node, target_node):
        # Set of visited nodes to prevent loops
        visited = set()
        queue = Queue()

        # Add the start_node to the queue and visited list
        queue.put(start_node)
        visited.add(start_node)
        
        # start_node has not parents
        parent = dict()
        parent[start_node] = None

        # Perform step 3
        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target_node:
                path_found = True
                break

            for (next_node, weight) in self.adjList[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    
        # Path reconstruction
        path = []
        if path_found:
            path.append(target_node)
            while parent[target_node] is not None:
                path.append(parent[target_node]) 
                target_node = parent[target_node]
            path.reverse()
        return path


    def bfs_traversal(self, start_node):
        visited = set()
        queue = Queue()
        queue.put(start_node)
        visited.add(start_node)

        while not queue.empty():
            current_node = queue.get()
            print(current_node, end = " ")
            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)  
                    

def shortestPath(type, graph, start, end):
    if type == 'DFS':
        return graph.DFS(start, end, [])
    elif type == 'BFS':
        return graph.BFS(start, end)
    return FileNotFoundError
 
 
# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()
 
 
if __name__ == '__main__':
 
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 4, 10),
            (4, 5, 1), (5, 4, 3), (1, 3, 2), (4, 3, 2), (1, 3, 5)]
 
    # No. of vertices (labelled from 0 to 5)
    n = 6
 
    # construct a graph from a given list of edges
    graph = Graph(edges, n)
 
    # print adjacency list representation of the graph
    printGraph(graph)

    start = 0
    end = 5
    print(shortestPath('DFS', graph, start, end))

    print(shortestPath('BFS', graph, start, end))

