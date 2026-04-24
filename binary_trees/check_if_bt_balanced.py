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

def height(root) :
	#Your code goes here
    if root == None:
        return 0
    leftlargest = 1 + height(root.left)
    rightlargest = 1 + height(root.right)
    largest = max(leftlargest,rightlargest)
    return largest    
def isBalanced(root):
    if root ==None:
        return True
    leftheigth = height(root.left)
    rightheight = height(root.right)
    if leftheigth - rightheight > 1 or rightheight - leftheigth >1:
        return True
    isleftBalanced = isBalanced(root.left)
    isrightBalanced = isBalanced(root.right)
    if isleftBalanced and isrightBalanced:
        return True
    else:
        return False

root = TakeInput()
printTree(root)
print(isBalanced(root))