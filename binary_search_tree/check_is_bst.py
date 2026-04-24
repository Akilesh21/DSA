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

def minTree(root):
    if root == None:
        return 100000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin,rightmin,root.data)
def maxTree(root):
    if root == None:
        return -100000
    leftmin = maxTree(root.left)
    rightmin = maxTree(root.right)
    return max(leftmin,rightmin,root.data)

def checkisbstSolution1(root):
    if root == None:
        return True
    if root.data > root.left.data and root.data < root.right.data :
        return True
    if checkisbstSolution1(root.left) and checkisbstSolution1(root.right):
        return True
    else:
        return False

def checkisbstSolution2(root):
    if root == None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data <= leftMax :
        return False
    isLeftBst = checkisbstSolution2(root.left)
    isrightBst = checkisbstSolution2(root.right)
    return isLeftBst and isrightBst
def checkisbstSolution3(root):
    if root==None:
        return 100000,-100000,True
    leftMin,leftMax,isLeftBST=checkisbstSolution3(root.left)
    rightMin,rightMax,isRightBST=checkisbstSolution3(root.right)
    
    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    isTreeBST=True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST=False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST=False
        
    return minimum,maximum,isTreeBST
def checkisbstSolution4(root,min_range,max_range):
    if root==None:
        return True
    if root.data<min_range or root.data>max_range:
        return False
    
    isLeftWithinConstraints=checkisbstSolution4(root.left,min_range,root.data-1)
    isRightWithinConstraints=checkisbstSolution4(root.right,root.data,max_range)
    
    return isLeftWithinConstraints and isRightWithinConstraints
root  =  TakeInput() 
print(checkisbstSolution1(root))
print(checkisbstSolution2(root))
print(checkisbstSolution3(root))
print(checkisbstSolution4(root,-10000,10000))