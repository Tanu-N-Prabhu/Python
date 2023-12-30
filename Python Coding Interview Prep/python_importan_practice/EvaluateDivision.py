"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # Step 1: Build the graph with values
        graph = defaultdict(dict)

        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value

        # Step 2: Perform DFS to find query results
        def dfs(node, target, visited):
            if node not in graph:
                return -1.0

            if target in graph[node]:
                return graph[node][target]

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return graph[node][neighbor] * result

            return -1.0

        results = []
        for query in queries:
            start, end = query
            if start in graph and end in graph:
                visited = set()
                result = dfs(start, end, visited)
                results.append(result)
            else:
                results.append(-1.0)

        return results


# Test cases
solution = Solution()
equations1 = [["a", "b"], ["b", "c"]]
values1 = [2.0, 3.0]
queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(solution.calcEquation(equations1, values1, queries1))  # Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values2 = [1.5, 2.5, 5.0]
queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(solution.calcEquation(equations2, values2, queries2))  # Output: [3.75000,0.40000,5.00000,0.20000]

equations3 = [["a", "b"]]
values3 = [0.5]
queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
print(solution.calcEquation(equations3, values3, queries3))  # Output: [0.50000,2.00000,-1.00000,-1.00000]

