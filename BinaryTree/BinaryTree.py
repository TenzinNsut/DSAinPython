
# Convention:  left-subtree - Root - right-subtree


class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


     
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
# print(node2.key) - > 5


# connecting left and right to root node
node0.left = node1
node0.right = node2
# print(node0.left.key) - > 4

# track root node
tree = node0
# print(tree.key) - > 3
# print(tree.left.key) - > 4
# print(tree.right.key) -> 5







