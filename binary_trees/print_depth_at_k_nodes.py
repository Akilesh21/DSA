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
def print_depth_at_k(root,k):
    if root ==None:
        return 
    if k ==0:
        print(root.data)
        return 
    print_depth_at_k(root.left,k-1)
    print_depth_at_k(root.right,k-1)

def print_depth_at_kv1(root,k,d):
    if root ==None:
        return 
    if k ==d:
        print(root.data)
        return 
    print_depth_at_k(root.left,k,d+1)
    print_depth_at_k(root.right,k,d+1)    

root = TakeInput()
printTree(root)
print_depth_at_k(root,2)
# print_depth_at_kv1(root,2,0)