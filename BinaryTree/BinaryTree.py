
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# H e i g h t  || D e p t h  
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

# D I A M E T E R  - > Longest path between two leaf nodes:
    def diameter(self):
        if self is None:
            return 0

# get the height of left and right subtree
        left_height = TreeNode.height(self.left)
        right_height = TreeNode.height(self.right)

        distance = left_height + right_height

# get the diameter of left and right subtree
        left_diameter = TreeNode.diameter(self.left)
        right_diameter = TreeNode.diameter(self.right)

# Compare the two and pick the max value
        return max(distance, max(left_diameter, right_diameter))

# N u m b e r - Of - N o d e s :
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

# M i n - D e p t h :
    def min_depth(self):
        if self is None:
            return 0
        
        elif self.left is None:
            return 1 + TreeNode.min_depth(self.right)

        elif self.right is None:
            return 1 + TreeNode.min_depth(self.left)


        return 1 + min(TreeNode.min_depth(self.left), TreeNode.min_depth(self.right))


# T r a v e r s a l :
    def inorder_traversal(self):
        if self is None:
            return []
        return (TreeNode.inorder_traversal(self.left)+[self.key]+TreeNode.inorder_traversal(self.right))

    def preorder_traversals(self):
        if self is None:
            return []
        return ([self.key]+TreeNode.preorder_traversals(self.left)+TreeNode.preorder_traversals(self.right))

    def postorder_traversal(self):
        if self is None:
            return []
        return (TreeNode.postorder_traversal(self.left)+TreeNode.postorder_traversal(self.right)+[self.key])




# SIMPLE WAY OF CONNECTING NODE:
# We will be using "tuples" in order to "connect nodes"
# Convention: left-subtree, root/parent, right-subtree
    @staticmethod
    def parse_tuple(data):
        # if node is empty/none then assing it as "None"
        if(data is None):
            node = None
        # "isinstace" checks if "argument passed" is of type "typle"
        elif(isinstance(data, tuple) and len(data) == 3):
        # To understand each recusive call 
            # print(data)

        # "data parsed" is of size 3, then mid_index should be "root-node"/"parent-node"
        # By convention, left-subtree, root/parent, right-subtree
        
            node = TreeNode(data[1]) # - > root/parent node

        # recusively, calling "parse_tuple" in order to parse "subtree's(left, right)"
            node.left = TreeNode.parse_tuple(data[0]) # - > left-subtree
            node.right = TreeNode.parse_tuple(data[2]) # - > right-subtree

    # if last/leaf node has some value then, parse it to TreeNode(class)
        else:
            node = TreeNode(data) 
        return node

# Driver code:
data = ((1,3,None),2,((None,3,4),5,(6,7,8)))
tree = TreeNode.parse_tuple(data)


# OUTPUT:
print("Height:",tree.height()) # - > Height: 4
print("Min-Depht:",tree.min_depth()) # - > Min-Depht: 3
print("Diameter:",tree.diameter()) # - > Diameter: 5
print("Number of nodes:",tree.size()) # - > Number of nodes: 9
print("Inorder:",tree.inorder_traversal()) # - > Inorder: [1, 3, 2, 3, 4, 5, 6, 7, 8]
print("Preorder:",tree.preorder_traversals()) # - > Preorder: [2, 3, 1, 5, 3, 4, 7, 6, 8]
print("Postorder:",tree.postorder_traversal()) # - > Postorder: [1, 3, 4, 3, 6, 8, 7, 5, 2]

      
