

# signature code:

class BST:
    # constructor:
    def __init__(self,initialvalue=None):
        self.value = initialvalue
        # initialy node is empty -> set its respective: left,right = None
        if(self.value == None):
            self.left = None
            self.right = None
        else:
            self.left = BST()
            self.right = BST()

    def insert(self,key):
        # if node is empty -> insert the 'key/value'
        if self.value is None:
            self.value = key
            # after insertion, create its respective left & right child
            self.left = BST()
            self.right =BST()
            return
        else:
            if(self.value == key):
                print(key,"already exits")
                return
            # Convention:  left-subtree < root < right-subtree
            if(self.value < key): 
                self.left.insert(key)
                return
            else:
                self.left.insert(key)
                return
            


    def inorder(self):
        if self.value is None:
            return ([])
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())

    def __str__(self):
        return (str(inorder()))



    def preorder(self):
        if self.value is None:
            return ([])
        else:
            return([self.value]+self.left.preorder()+self.right.preorder())
    
    def __str__(self):
        return (str(preorder()))



    def postorder(self):
        if self.value is None:
            return ([])
        else:
            return(self.left.postorder()+self.right.postorder()+[self.value])

    def __str__(self):
        return (str(postorder()))


    
    def find(self,key):
        if self.key == key:
            return f"{self.key} exists."
        if(self.key > key):
            self.left.find(key)
            return
        else:
            self.right.find(key)
            return