class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTree(root):        
    if root == None:
        return 
    print(root.data,end=":")
    if root.left != None:
        print("L",root.left.data,end=",")
    if root.right != None:
        print("R",root.right.data,end=" ")
    print()
    printTree(root.left)
    printTree(root.right)
def TakeInput():    
    rootData = int(input())
    if rootData ==-1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = TakeInput()
    rightTree = TakeInput()
    root.left = leftTree
    root.right = rightTree
    return root
def remove_leaf_node(root):
    if root == None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove_leaf_node(root.left)
    root.right = remove_leaf_node(root.right)
    return root

root = TakeInput()
printTree(root)
remove_leaf_node(root)
printTree(root)
