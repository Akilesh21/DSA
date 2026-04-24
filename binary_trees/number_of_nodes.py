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
def number_of_nodes(root):
    if root == None:
        return 0
    leftCount  = number_of_nodes(root.left)
    rightCount = number_of_nodes(root.right)
    return 1+leftCount+rightCount
root = TakeInput()
printTree(root)
print(number_of_nodes(root))