"""
                    Traversals:

#    Traversal is a process of visiting each node of a binary tree exactly once.
# - > we keep track of visted nodes, by using a "visited_list[]" and then, return the list.

# There are three kinds of traversals:
1.)Inorder: left-subtree, root/parent, right-subtree
3.)Preorder: root/parent, left-subtree, right-subtree
2.)Postorder: left-subtree, right-subtree, root/parent


# signature fuction:

def inorder_traversal(node):
    if node is None:
        return []
    return(inorder_traversal(node.left)+[node.key]+inorder_traversal(node.right))


"""


class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None



# traversal functions/methods:
def inorder_traversal(node):
    if node is None:
        return []
    return(inorder_traversal(node.left)+[node.key]+inorder_traversal(node.right))

def preorder_traversal(node):
    if node is None:
        return []
    return([node.key]+preorder_traversal(node.left)+preorder_traversal(node.right))

def postorder_traversal(node):
    if node is None:
        return []
    return(postorder_traversal(node.left)+postorder_traversal(node.right)+[node.key])


def parse_data(data):
    if(isinstance(data, tuple) and len(data) ==3):
        node = TreeNode(data[1]) 
        node.left = parse_data(data[0])
        node.right = parse_data(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


# driver code :
data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree = parse_data(data)



print("Inorder:",inorder_traversal(tree))
print("Postorder:",postorder_traversal(tree))
print("Preorder:",preorder_traversal(tree))