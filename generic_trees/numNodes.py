class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    print()    
    for child in root.children:
        printTreeDetailed(child) 
def takeTreeInput():
    print("Enter the root:")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("How many children you want for:",rootData)
    children = int(input())
    for i in range(children):
        child = takeTreeInput()
        root.children.append(child)
    return root    
def numNodes(root):
    if root==None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count
root = takeTreeInput()
printTreeDetailed(root)
print(numNodes(root))    