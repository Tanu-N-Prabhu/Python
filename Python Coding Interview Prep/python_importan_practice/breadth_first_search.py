graph = {
    'Frankfurt': ['Mannhem', 'Wurzburg', 'Kassel'],
    'Mannhem': ['Kurlsruhe'],
    'Kurlsruhe': ['Augsburg'],
    'Kassel': ['Munchen'],
    'Wurzburg': ['Erfurt', 'Numberg'],
    'Numberg': ['Stutgurt'],
    'Erfurt': [],
    'Stutgurt': [],
    'Munchen': [],
    'Augsburg': []
}

# just printing the whole graph tree
for key, val in graph.items():
    print((key, val))

visited = []  # List to keep track of visited nodes.
queue = []     # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" -> ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("\nBreadth first search result\n")
# Driver Code
bfs(visited, graph, 'Frankfurt')
