# create the class Node and the attrbutes 
class Node:
    def __init__(self, letter):
        self.left = None
        self.right = None
        self.data = letter

# in order traversal left, root, right
# O(n)
def InOrd(root):
    if root:
        InOrd(root.left)
        print(root.data)
        InOrd(root.right)

# pre order traversal root, left, right
# O(n)
def PreOrd(root):
    if root:
        print(root.data)
        PreOrd(root.left)
        PreOrd(root.right)

# post order traversal left, right, root
# O(n)
def PostOrd(root):
    if root:
        PostOrd(root.left)
        PostOrd(root.right)
        print(root.data)


# Function to get the count of leaf nodes in binary tree
def getLeafCount(node):
    if node is None:
        return 0 
    # it is a child node
    if(node.left is None and node.right is None):
        return 1 
    else:
        # recursively call
        return getLeafCount(node.left) + getLeafCount(node.right)


# create the nodes for the tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print("in order")
InOrd(root)
print("pre order")
PreOrd(root)
print("post order")
PostOrd(root)
print(getLeafCount(root))
