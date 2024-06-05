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

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return sum([w for u, v, w in result]), result

def min_sum_of_edge_lengths(n, m, s):
    if m == n - 1:
        return s

    base_graph = Graph(n)

    # Create a base MST with n-1 edges and total weight `s`
    edges_needed = n - 1
    base_weight = s // edges_needed
    remainder = s % edges_needed

    for i in range(edges_needed):
        weight = base_weight + (1 if i < remainder else 0)
        base_graph.add_edge(i, i + 1, weight)

    mst_value, mst_edges = base_graph.kruskal_mst()

    total_edges = mst_edges[:]

    # Add extra edges with minimal weight (1)
    for i in range(m - (n - 1)):
        total_edges.append([0, 0, 1])

    # Calculate the total sum of all edges
    total_sum = sum([weight for u, v, weight in total_edges])
    
    return total_sum


if __name__ == '__main__':
    # q = int(input().strip())

    # for _ in range(q):
    #     n, m, s = map(int, input().strip().split())
    #     print(min_sum_of_edge_lengths(n, m, s))

    test_cases = [
        ("1\n4 5 4", "7\n"),
        ("1\n4 3 6", "6\n"),
        ("1\n3 3 2", "3\n"),
        ("1\n5 7 10", "12\n"),
        ("1\n2 1 1", "1\n"),
        ("2\n3 2 2\n4 6 5", "2\n7\n")
        ]

    for i, (input_data, expected_output) in enumerate(test_cases):
        input_lines = input_data.split('\n')
        output = []
        
        input_mock = lambda: input_lines.pop(0)
        input = input_mock
        
        n_cases = int(input())
        
        for _ in range(n_cases):
            n, m, s = map(int, input().split())
            mst = min_sum_of_edge_lengths(n, m, s)
            print(mst)
            output.append(str(mst))
        
        result = "\n".join(output) + "\n"
        
        print(f"Test Case {i + 1}: {'Passed' if result == expected_output else 'Failed'}")
