class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
def printTree(root):
    #  In generic Tree we don't need any base case since every children can't be None
    # if it is None means we have to go through every node like binary Tree
    # Not a base case but an edge Case
    if root == None:
        return 
    print(root.data)
    for child in root.children:
        printTree(child)        
# Since in uper function we can't tell connection between the root and children         
def printTreeDetailed(root):        
    if root == None:
        return
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,",",end="")
    for child in root.children:
        printTreeDetailed(child)    