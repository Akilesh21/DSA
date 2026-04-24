class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

b = BinaryTreeNode(1)
b1 = BinaryTreeNode(2)
b2 = BinaryTreeNode(3)
b.left = b1
b.right = b2
print(b.data,b.left.data,b.right.data)
b4 = BinaryTreeNode(5)
b1.left = b4
print(b.left.left.data)