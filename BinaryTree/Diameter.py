class TreeNode:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None



# H e i g h t  || D e p t h  

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))
        

# D I A M E T E R  - > Longest path between two leaf nodes
def diameter(root):
    if root is None:
        return 0
            
# get the height of left and right subtree
    lh = height(root.left)
    rh = height(root.right)
        
    distance = lh + rh 
         
# get the diameter of left and right subtree
    dl = diameter(root.left)
    dr = diameter(root.right)
        
# Compare the two and pick the max value
    return max(distance, max(dl,dr))
    
            

# M i n - D E P T H -
def min_height(root):
    if(root is None):
        return 0
            
    # elif root.left is None and root.right is None:
    #     return 1
            
    elif root.right is None:
        return min_height(root.left)+1
            
    elif root.left is None:
        return min_height(root.right)+1
            
            
    return 1 + min(min_height(root.left),min_height(root.right))



# N u m b e r - Of - N o d e s 
def tree_size(node):
    if node is None:
        return 0
    return 1 +  tree_size(node.left) + tree_size(node.right)




def parse_data(data):
    if(isinstance(data,tuple) and len(data) == 3):
        node = TreeNode(data[1])
        node.left = parse_data(data[0])
        node.right = parse_data(data[2])
    
    elif(data is None):
        node = None
    else:
        node = TreeNode(data)
    return node


data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree = parse_data(data)
    
print("Depth : ",height(tree))
print("Number of nodes : ",tree_size(tree))
print("Diameter : ",diameter(tree))
print("Min Depht : ",min_height(tree))