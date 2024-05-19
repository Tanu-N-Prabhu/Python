"""
Allison loves graph theory and just started learning about Minimum Spanning Trees(MST). 
She has three integers, n, m, and s, and uses them to construct a graph with the following properties:
• The graph has n nodes and m undirected edges where each edge has a positive integer length.
• No edge may directly connect a node to itself, and each pair of nodes can only be directly connected 
by at most one edge.
• The graph is connected, meaning each node is reachable from any other node.
• The value of the minimum spanning tree is s. Value of the MST is the sum
of all the lengths of all edges of which are part of the tree.
• The sum of the lengths of all edges is as small as possible.

graph

a,b = 2
a,c = 1
b,d = 2
c,d = 1
a,d = 1


For example, let's say n = 4. m = 5 and 8 = 4. We need to construct a graph with 4 nodes and 5 edges. The value of minimum spanning tree must be 4. The diagram belows shows a way to construct such a graph while keeping the lengths of all edges is as small as possible:

For example, let's say ,  and . We need to construct a graph with  nodes and  edges. The value of minimum spanning tree must be . The diagram belows shows a way to construct such a graph while keeping the lengths of all edges is as small as possible:**

[//]: # "image"

Here the sum of lengths of all edges is .

Given **q**, **n**, **m** and **x** for **q** graphs satisfying the conditions above, find and print the minimum sum of the lengths of all the edges in each graph on a new line.

Input Format

The first line contains an integer, **q**, denoting the number of graphs.

Each of the **q** subsequent lines contains three space-separated integers describing the respective values of **n** (the number of nodes in the graph), **m** (the number of edges in the graph), and **x** (the value of the MST graph).

Constraints

For **q** of the maximum score:

[//]: # "For  of the maximum score:"

[//]: # "For  of the maximum score:"

[//]: # "For  of the maximum score:"

[//]: # "For  of the maximum score:"

Output Format

For each graph, print an integer on a new line denoting the minimum sum of 
the lengths of all edges in a graph satisfying the given conditions.

Sample Input

2
4 5 4
4 3 6


Sample Output

7
6


Explanation

Graph 1:
The answer for this sample is already explained in the problem statement.

Graph 2:
We must construct a graph with 4 nodes, 3 edges, and an MST value of 6. 
Recall that a connected graph with 4 nodes and 3 edges is already a tree, 
so the MST will contain all 3 edges and the total length of all the edges of the graph will be equal 
to the value of the minimum spanning tree. So the answer is 6.
"""

#!/bin/python3
import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] \
                        and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return sum(key)

def min_sum_of_edge_lengths(n, m, s, graph):
    if m >= n - 1:
        return s
    else:
        return graph.primMST()

if __name__ == '__main__':
    g = int(input("Enter the number of test cases: "))

    for _ in range(g):
        n, m, s = map(int, input().split())
        
        # Construct the graph
        graph = Graph(n)
        for _ in range(m):
            u, v, weight = map(int, input().split())
            graph.graph[u - 1][v - 1] = weight
            graph.graph[v - 1][u - 1] = weight

        # Print the minimum sum of edge lengths
        print(min_sum_of_edge_lengths(n, m, s, graph))
