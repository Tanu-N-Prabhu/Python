# Using a Python dictionary to act as an adjacency list
graph = {
  'Frankfruit' : ['Mannhem','Wurzburg','Kassel'],
  'Mannhem' : ['Kurlsruhe'],
  'Kurlsruhe' : ['Augsburg'],
  'Kassel' : ['Munchen'],
  'Wurzburg' : ['Erfurt','Numberg'],
  'Numberg' : ['Stutgurt'],
  'Erfurt' : [],
  'Stutgurt' : [],
  'Munchen' : [],
  'Augsburg' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" -> ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'Frankfruit')