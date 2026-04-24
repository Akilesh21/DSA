from queue import Queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
  
def takeTreeInputLevelWise():
    q=Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        
        print("Enter right child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root
   
def printLevelWise(root):
    q = Queue()    

    if root == None:
        return None
    
    q.put(root)
    
    while (not(q.empty())):
        a = q.get()
        print(a.data, end = ":")
        
        leftChild = a.left
        if leftChild != None:
            print("L:", end = "")
            print(leftChild.data, end = ",")
            q.put(leftChild)
        else:
            print("L:", end = "")
            print(-1, end = ",")
            
        rightChild = a.right
        if rightChild != None:
            print("R:", end = "")
            print(rightChild.data)
            q.put(rightChild)
        else:
            print("R:", end = "")
            print(-1)
                      
    return root
def buildTreeFromposIn(ino,pos):
    if len(pos)==0:
        return None
    rootData = pos[len(pos)-1]
    root = BinaryTreeNode(rootData)
    rootIndexInorder = -1
    for i in range(0,len(ino)):
        if ino[i]==rootData:
            rootIndexInorder = i
            break
    if rootIndexInorder ==-1:
        return None
    leftinorder = ino[0:rootIndexInorder]
    rightInorder = ino[rootIndexInorder+1:]
    lenleftsubtree = len(leftinorder)   

    leftPosorder = pos[0:lenleftsubtree+1]
    rightPosorder = pos[lenleftsubtree+1:len(pos)-1]
    leftchild  =buildTreeFromposIn(leftinorder,leftPosorder)
    rightchild = buildTreeFromposIn(rightInorder,rightPosorder)
    root.left = leftchild
    root.right = rightchild
    return root
def print_without_levelwise(root):
    if root is None:
        return None
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not  None:
        print("R",root.right.data,end="")
    print()
    print_without_levelwise(root.left)
    print_without_levelwise(root.right)   
pos = [4,5,2,6,7,3,1]
ino = [4,2,5,1,6,3,7]
root = buildTreeFromposIn(ino,pos)
print_without_levelwise(root)