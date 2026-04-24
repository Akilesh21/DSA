class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    # function we want in our bst are 
    # 1) isPresent or search
    # 2) insert : to insert the element in the tree
    # 3) delete : to delete the element
    # 4) count : count the height of the tree
    def __init__(self):
        self.root = None
        self.numNodes = 0
    def printTreeHelper(self,root):
        if root==None:
            return
        print(root.data,end=":")
        if root.left!=None:
            print("L:", end='')
            print(root.left.data, end=',')
            #print("L",root.left.data,end=",")
        if root.right!=None:
            print("R:", end='')
            print(root.right.data, end='')
            #print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    def printTree(self):
        self.printTreeHelper(self.root)        
    def isPresentHelper(self,root,data):
        if root == None:
            return False
        if root.data == data :
            return True
        if root.data > data:
            # call on left
            return self.isPresentHelper(root.left,data)
        else:
            # call on right
            return self.isPresentHelper(root.right,data) 
    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)
    def insertHelper(self,root,data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data >= data:
            root.left = self.insertHelper(root.left,data)
            return root
        else:
            root.right = self.insertHelper(root.right,data)  
            return root  
    def insert(self,data):
        self.numNodes +=1
        self.root = self.insertHelper(self.root,data)
      
    def insert(self,data):
        self.numNodes +=1
        self.root = self.insertHelper(self.root,data)
    def min(self,root):
        if root == None:
            return 100000
        if root.left == None:
            return root.data
        return self.min(root.left)   
    def deletehelper(self,root,data):
        if root == None:
            return False,None
        if root.data < data:
            deleted,newRightNode = self.deletehelper(root.right,data)
            root.right = newRightNode 
            return deleted,root
        if root.data > data:
            deleted,newleftNode = self.deletehelper(root.left,data)
            root.left = newleftNode  
            return deleted,root  
        # root is leaf first case
        if root.left == None and root.right == None:
            return True,None
        # root have one child second case
        if root.left == None:
            return True,root.right
        
        if root.right == None:
            return True,root.left
        # root have two child third case
        replacement = self.min(root.right)
        root.data = replacement
        deleted,newRightNode = self.deletehelper(root.right,replacement)
        root.right = newRightNode
        return True,root
    def delete(self,data):
        deleted,newRoot = self.deletehelper(self.root,data)
        if deleted:
            self.numNodes -=1
        self.root = newRoot     
        return deleted
    def count(self):
        return self.numNodes
b = BST()
b.insert(1)
b.insert(7)
b.insert(4)    
b.delete(1)
b.printTree()