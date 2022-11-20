

class TreeNode:
    def __init__(self, value):
        self.value =  value
        self.right = None
        self.left = None


def parse_data(data):
    # "isinstace" checks if "argument passed" is of type "typle"
    if(isinstance(data, tuple) and len(data) == 3):
        # To understand each recusive call 
        print(data)

        # "data parsed" is of size 3, then mid_index should be "root-node"/"parent-node"
        # By convention, left-subtree, root/parent, right-subtree
        
        node = TreeNode(data[1]) # - > root/parent node

        # recusively, calling "parse_data" in order to parse "subtree's(left, right)"
        node.left = parse_data(data[0]) # - > left-subtree
        node.right = parse_data(data[2]) # - > right-subtree

    # if node is empty/none then assing it as "None"
    elif(data is None):
        node = None
    # if last/leaf node has some value then, parse it to TreeNode(class)
    else:
        node = TreeNode(data) 
    return node





# Driver code:

data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree = parse_data(data)
print("========= A N S W E R ==========")
print("Node is:",tree.right.right.value) # - > 7


    
