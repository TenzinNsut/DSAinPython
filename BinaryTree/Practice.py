# https://www.youtube.com/watch?v=pkYVOmU3MgA&t=4142s
#  time-stamp  = 3:17:07

# Manually connecting each node 

class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


root = BinaryTree(2)


node1 = BinaryTree(1)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)
node8 = BinaryTree(8)

node_3 = BinaryTree(3)



# connected root with left and right nodes
root.left = node3
root.right = node5



# similarly, connecting rest of the ndoes
node3.left = node1
node3.right = None


node5.left = node_3
node5.right = node7

node_3.left = None
node_3.right = node4

node7.left = node6
node7.right = node8



# so now tree is the root node
tree = root




# print(tree.left.key) # - > 3
# print(tree.left.left.key) # - > 1
# print(tree.right.right.key) #  - > 7
# print(tree.right.right.right.key)# - >8



"""
WORKS !!!
"""