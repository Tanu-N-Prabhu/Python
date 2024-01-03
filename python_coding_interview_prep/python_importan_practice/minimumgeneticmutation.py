"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2


Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank = set(bank)
        mutations = {'A', 'C', 'G', 'T'}
        queue = deque([(startGene, 0)])

        while queue:
            current_gene, mutations_count = queue.popleft()

            if current_gene == endGene:
                return mutations_count

            for i in range(len(current_gene)):
                for mutation in mutations:
                    if mutation == current_gene[i]:
                        continue
                    new_gene = current_gene[:i] + mutation + current_gene[i + 1:]
                    if new_gene in bank:
                        queue.append((new_gene, mutations_count + 1))
                        bank.remove(new_gene)

        return -1


# Test cases
solution = Solution()
startGene1 = "AACCGGTT"
endGene1 = "AACCGGTA"
bank1 = ["AACCGGTA"]
print(solution.minMutation(startGene1, endGene1, bank1))  # Output: 1

startGene2 = "AACCGGTT"
endGene2 = "AAACGGTA"
bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(solution.minMutation(startGene2, endGene2, bank2))  # Output: 2

