class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("Enter number of children for ",rootData)
    childrencount = int(input())
    for i in range(childrencount):
        child = takeTreeInput()
        root.children.append(child)
    return root    
def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        printTreeDetailed(child)            
root = takeTreeInput()
printTreeDetailed(root)