"""
You are given a string  and your task is to make the string increasing. 
A string  is called increasing if the following is true:

      ∀j, k : j < k →  ≤j <= sk 

i.e., the ASCII value of every character of the given string S is less than or equal to 
any of its preceding characters.

Given the cost of changing every character to every other character, 
what is the minimum cost to make a given string  increasing?

Input Format

The first line contains an integer,T , the number of test cases. T test cases follow, each containing  
27 lines:
The first line of each test case, contains the string S.
Each of the next 26 lines contain 26 space-separated integers. The first line is cost of changing one  
a to any other letter, the second line is the cost of changing one b to any other letter, and so on.
Diagonal of this 26 x 26 table will be zero (there is no cost if you don't change a letter).

Constraints
1 <= T <= 25
1 <= length of string <= 1991
0 <= cost of changing letters <= 100
Input string contains only lower case letters 'a' to 'z'.

Output Format

For each test case, print in a new line the minimum cost and the increasing string you made 
using minimum cost, separated with a space.
If there are several such strings, print the lexicographically smallest string.

Sample Input

1
mehdi
0 87 55 45 15 50 35 34 40 96 90 57 77 92 80 18 56 53 19 78 11 13 74 65 8 16
89 0 48 39 59 74 7 21 6 66 18 75 19 13 95 38 32 67 75 92 38 72 58 59 86 94
88 76 0 8 30 91 79 67 91 23 25 72 37 12 98 30 2 47 12 69 21 36 12 98 84 42
59 3 80 0 87 80 7 98 54 19 4 49 45 41 11 5 76 67 32 25 3 40 47 84 24 19
90 52 73 68 0 31 25 99 10 84 37 43 81 62 64 31 69 3 94 68 2 55 42 98 57 32
21 85 91 17 60 0 32 1 56 38 71 12 39 61 16 25 33 15 1 55 57 20 31 72 55 66
43 66 38 39 74 63 0 84 18 9 63 67 1 15 44 64 18 65 50 62 93 96 32 54 57 49
95 41 13 67 26 33 76 0 98 73 39 88 47 9 16 47 68 96 66 0 81 54 94 73 11 20
12 40 60 44 39 51 88 60 0 97 51 42 5 93 41 9 91 71 72 93 96 47 49 33 66 14
44 99 13 82 22 2 56 73 15 0 66 19 95 91 29 5 83 31 56 7 82 85 93 92 50 0
48 74 83 4 24 46 51 10 99 59 0 15 62 81 64 96 22 29 2 23 10 28 20 17 9 2
70 30 39 81 77 32 35 9 45 10 99 0 1 6 17 29 8 75 35 93 32 43 34 20 61 18
71 83 53 96 28 28 71 88 55 76 14 44 0 36 34 67 59 41 30 5 19 91 94 43 24 68
58 19 61 15 26 35 73 43 23 85 17 12 93 0 11 68 94 75 78 62 60 76 42 46 4 99
55 22 87 85 86 92 63 73 19 82 99 83 18 57 0 63 57 11 71 69 63 2 66 71 57 71
96 30 66 83 88 82 47 79 49 91 73 12 6 52 31 0 52 38 81 87 38 9 38 11 4 42
34 55 17 18 30 49 69 8 79 96 65 15 81 93 86 38 0 88 22 62 46 22 28 48 93 99
32 19 48 66 57 75 82 81 76 59 48 66 20 58 32 43 17 0 28 70 19 94 63 19 38 18
31 8 15 35 17 75 55 28 14 12 61 73 16 7 16 59 89 88 0 65 78 72 59 61 5 68
17 41 81 38 94 32 38 47 68 89 65 14 48 90 11 35 20 60 76 0 31 33 20 60 66 94
61 6 55 52 75 94 14 63 75 60 56 93 68 17 98 54 57 73 71 36 0 80 78 56 72 19
61 33 40 9 58 42 30 11 92 25 37 63 5 89 2 68 43 36 14 80 13 0 69 6 19 16
33 36 73 81 15 52 77 25 17 76 30 58 29 48 58 70 52 41 74 21 42 41 0 26 83 10
88 5 74 71 17 58 98 55 2 16 95 75 92 64 43 20 54 77 51 40 13 96 9 0 79 20
92 44 84 4 99 76 55 7 47 73 77 57 52 58 37 27 98 52 29 40 62 61 88 16 0 36
26 42 71 43 56 31 66 36 2 23 64 32 53 57 67 17 10 85 51 55 80 24 68 7 78 0
Sample Output

20 mrtuz
Explanation

m changes to m with cost 0
e changes to r with cost 3
h changes to t with cost 0
d changes to u with cost 3
i changes to z with cost 14
"""

from math import inf


def min_cost_increasing_string(T, test_cases):
    results = []
    
    for t in range(T):
        S = test_cases[t][0]
        costs = test_cases[t][1]
        n = len(S)
        dp = [[inf] * 26 for _ in range(n)]
        
        # Initialize the first column
        for i in range(26):
            dp[0][i] = costs[ord(S[0]) - ord('a')][i]
        
        # Dynamic Programming to calculate minimum costs
        for i in range(1, n):
            for j in range(26):
                for k in range(26):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[ord(S[i]) - ord('a')][j])
        
        # Backtrack to find the increasing string with minimum cost
        min_cost = min(dp[-1])
        min_string = []
        min_string.append(chr(dp[-1].index(min_cost) + ord('a')))
        prev_cost = min_cost
        
        for i in range(n - 2, -1, -1):
            for j in range(26):
                if dp[i][j] == prev_cost - costs[ord(S[i + 1]) - ord('a')][ord(min_string[-1]) - ord('a')]:
                    min_string.append(chr(j + ord('a')))
                    prev_cost = dp[i][j]
                    break
        
        results.append((min_cost, ''.join(reversed(min_string))))
    
    return results

# Sample Input
T = 1
test_cases = [
    ("mehdi", [
        [0, 87, 55, 45, 15, 50, 35, 34, 40, 96, 90, 57, 77, 92, 80, 18, 56, 53, 19, 78, 11, 13, 74, 65, 8, 16],
        [89, 0, 48, 39, 59, 74, 7, 21, 6, 66, 18, 75, 19, 13, 95, 38, 32, 67, 75, 92, 38, 72, 58, 59, 86, 94],
        [88, 76, 0, 8, 30, 91, 79, 67, 91, 23, 25, 72, 37, 12, 98, 30, 2, 47, 12, 69, 21, 36, 12, 98, 84, 42],
        [59, 3, 80, 0, 87, 80, 7, 98, 54, 19, 4, 49, 45, 41, 11, 5, 76, 67, 32, 25, 3, 40, 47, 84, 24, 19],
        [90, 52, 73, 68, 0, 31, 25, 99, 10, 84, 37, 43, 81, 62, 64, 31, 69, 3, 94, 68, 2, 55, 42, 98, 57, 32],
        [21, 85, 91, 17, 60, 0, 32, 1, 56, 38, 71, 12, 39, 61, 16, 25, 33, 15, 1, 55, 57, 20, 31, 72, 55, 66],
        [43, 66, 38, 39, 74, 63, 0, 84, 18, 9, 63, 67, 1, 15, 44, 64, 18, 65, 50, 62, 93, 96, 32, 54, 57, 49],
        [95, 41, 13, 67, 26, 33, 76, 0, 98, 73, 39, 88, 47, 9, 16, 47, 68, 96, 66, 0, 81, 54, 94, 73, 11, 20],
        [12, 40, 60, 44, 39, 51, 88, 60, 0, 97, 51, 42, 5, 93, 41, 9, 91, 71, 72, 93, 96, 47, 49, 33, 66, 14],
        [44, 99, 13, 82, 22, 2, 56, 73, 15, 0, 66, 19, 95, 91, 29, 5, 83, 31, 56, 7, 82, 85, 93, 92, 50, 0],
        [48, 74, 83, 4, 24, 46, 51, 10, 99, 59, 0, 15, 62, 81, 64, 96, 22, 29, 2, 23, 10, 28, 20, 17, 9, 2],
        [70, 30, 39, 81, 77, 32, 35, 9, 45, 10, 99, 0, 1, 6, 17, 29, 8, 75, 35, 93, 32, 43, 34, 20, 61, 18],
        [71, 83, 53, 96, 28, 28, 71, 88, 55, 76, 14, 44, 0, 36, 34, 67, 59, 41, 30, 5, 19, 91, 94, 43, 24, 68],
        [58, 19, 61, 15, 26, 35, 73, 43, 23, 85, 17, 12, 93, 0, 11, 68, 94, 75, 78, 62, 60, 76, 42, 46, 4, 99],
        [55, 22, 87, 85, 86, 92, 63, 73, 19, 82, 99, 83, 18, 57, 0, 63, 57, 11, 71, 69, 63, 2
