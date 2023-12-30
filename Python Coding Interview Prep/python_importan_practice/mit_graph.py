class Node(object):
	def __init__(self, name):
		"""assume name is a string"""
		self.name = name

	def getName(self):
		return self.name

	def __str__(self):
		return self.name


class Edge(object):
	def __init__(self, src, dest):
		"""
		assume src and dest are nodes
		src node -> dest node
		"""
		self.src = src
		self.dest = dest

	def getSource(self):
		return self.src

	def getDestination(self):
		return self.dest

	def __str__(self):
		return self.src.getName() + ' -> '\
			+ self.dest.getName()


class Diagraph(object):
	"""
	Edge is a dict mapping each node to a list of its children
	"""
	def __init__(self):
		self.edges = {}

	def addNode(self, node):
		if node in self.edges:
			raise ValueError('Duplicate node')
		else:
			self.edges[node] = []

	def addEdge(self, edge):
		src = edge.getSource();
		dest = edge.getDestination()
		if not(src in self.edges and dest in self.edges):
			raise ValueError('node not in graph')
		self.edges[src].append(dest)

	def childrenOf(self, node):
		return self.edges[node]

	def hasNode(self, node):
		return node in self.edges

	def getNode(self, name):
		for n in self.edges:
			if n.getName() == name:
				return n
		raise NameError(name)

	def __str__(self):
		result = ''
		for src in self.edges:
			for dest in self.edges[src]:
				result = result + src.getName() + ' -> '\
					+ dest.getName() + '\n'
		return result[:-1] # omit final new line 


class Graph(Diagraph):
	def addEdge(self, edge):
		Diagraph.addEdge(self, edge)
		rev = Edge(edge.getDestination(), edge.getSource())
		Diagraph.addEdge(self, rev)


def buildCityGraph(graphType):
	g = graphType()
	for name in ('Boston', 'Province', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
		g.addNode(Node(name))

	g.addEdge(Edge(g.getNode('Boston'), g.getNode('Province')))
	g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Province'), g.getNode('Boston')))
	g.addEdge(Edge(g.getNode('Province'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
	g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
	g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

	return g


def DFS(graph, start, end, path, shortest, toPrint = False):
	path = path + [start]
	if toPrint:
		print('Current DFS path: ', printPath(path))
	if start == end:
		return path
	for node in graph.childrenOf(start):
		# avoid cycle
		if node not in path:
			if shortest == None or len(path) < len(shortest):
				newPath = DFS(graph, node, end, path, shortest, toPrint)
				if newPath != None:
					shortest = newPath
		elif toPrint:
			print('already visited',  node)
	return shortest

def shortestPath(type, graph, start, end, toPrint = False):
	if type == 'DFS':
		return DFS(graph, start, end, [], None, toPrint)
	elif type == 'BFS':
		return BFS(graph, start, end, toPrint)
	return FileNotFoundError

def testSP(source, destination):
	g = buildCityGraph(Diagraph)
	sp = shortestPath('DFS', g, g.getNode(source), g.getNode(destination), True)
	
	if sp != None:
		print('DFS shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
	else:
		print('DFS there is no path from ', source, ' to ', destination)

	sp = shortestPath('BFS', g, g.getNode(source), g.getNode(destination), True)
	
	if sp != None:
		print('BFS shortest path from ', source, ' to ', destination, ' is ', printPath(sp))
	else:
		print('BFS there is no path from ', source, ' to ', destination)

def printPath(node):
	res = ''
	for i in node:
		res = res + i.getName() + ' -> '
	return res[:-3]


def BFS(graph, start, end, toPrint = False):
	initPath = [start]
	pathQueue = [initPath]
	while len(pathQueue) != 0:
		# get the remove oldest element in pathQueue
		tmpPath = pathQueue.pop(0)
		if toPrint:
			print('current BFS path: ', printPath(tmpPath))
		lastNode = tmpPath[-1]
		if lastNode == end:
			return tmpPath
		for nextNode in graph.childrenOf(lastNode):
			if nextNode not in tmpPath:
				newPath = tmpPath + [nextNode]
				pathQueue.append(newPath)

	return None



if __name__ == "__main__":

	graph = buildCityGraph(Diagraph)
	print(graph)

	testSP('Boston', 'Phoenix')




