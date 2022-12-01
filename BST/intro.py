"""
                 BinarySearchTree:
Convention: left-subtree < root < right-subtree
"""

class BSTNode():
    # We are using "value"(optional), which will be using in th case of passing strings 
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None #will point to parent node, useful for upward traversal - > root
    
def insert(node,key,value):
    if node is None:
        node = BSTNode(key,value)
    elif(key < node.key):
        node.left = BSTNode(key,value)
        node.left.parent = node
    elif(key > node.key):
        node.right = BSTNode(key,value)
        node.right.parent = node
    return node

def find(node,key):
    if node is None:
        return None
    if(key == node.key):
        return node
    elif(key > node.key):
        return find(node.right, key)
    elif(key > node.key):
        return find(node.left, key)

def update(node,key,value):
    target = find(node, key)
    if target is None:
        target.value = value

# function to determine, if binary tree is balanced 


