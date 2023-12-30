
"""
Find the path by graph
"""
def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in graph.keys():
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath:
				return newpath
	return None


"""
Find all paths by graph
"""
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths



"""
Find the shortest path by graph
"""
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


"""
traverse the graph and check from one to another can go
"""
def reach(travel_graph, x, visited=None):
    if visited is None:
        visited = set() # see note
    visited.add(x)
    for y in travel_graph.get(x, []):
        if y not in visited:
            yield y
            for z in reach(travel_graph, y, visited):
                yield z


if __name__ == '__main__':

	# driver code
	graph = {'A': ['B', 'C'],
	             'B': ['C', 'D'],
	             'C': ['D'],
	             'D': ['C'],
	             'E': ['F'],
	             'F': ['C']}
	print(graph)

	x = 'D'
	for y in reach(graph, x):
		print("From {} you can go to {}".format(x, y))

	print(find_path(graph, 'A', 'D'))
	# ['A', 'B', 'C', 'D']

	print(find_all_paths(graph, 'A', 'D'))
	# [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]

	print(find_shortest_path(graph, 'A', 'D'))
	# ['A', 'B', 'D']


