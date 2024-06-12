"""
Given a list of accounts where each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person
if there is some common email to both accounts. Note that even if two accounts have the same name,
they may belong to different people as people could have the same name. A person can have any number
of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each
account is the name, and the rest of the elements are emails in sorted order. The accounts themselves
can be returned in any order.



Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""
from collections import defaultdict
from typing import List


class Solution:
    """
    This solution uses a graph to represent the accounts.
    The graph is represented by a dictionary where the keys are the emails and the values are the emails
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Depth-first search function to traverse connected emails
        def dfs(email, component):
            visited.add(email)  # Mark email as visited
            component.append(email)  # Add email to the current component
            for neighbor in graph[email]:  # Traverse neighbors of the current email
                if neighbor not in visited:  # If neighbor is not visited
                    dfs(neighbor, component)  # Recursively traverse neighbor

        email_to_name = {}  # Dictionary to map email to name
        graph = defaultdict(list)  # Graph to represent connections between emails

        # Populate email_to_name and graph
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].append(account[1])  # Add edge between email and account's first email
                graph[account[1]].append(email)  # Add edge between account's first email and email
                email_to_name[email] = name  # Map email to name

        visited = set()  # Set to store visited emails
        result = []  # List to store merged accounts

        # Traverse each email in the graph
        for email in graph:
            if email not in visited:  # If email is not visited
                component = []  # Initialize component for the current email
                dfs(email, component)  # Traverse connected emails
                # Append merged account to result list
                result.append([email_to_name[email]] + sorted(component))

        return result  # Return merged accounts


if __name__ == '__main__':
    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
        ]
    # Print the merged accounts using Solution class
    print(Solution().accountsMerge(accounts))
