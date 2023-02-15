class Node:
    __Slots__ = "element","left","right"
    
    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root = None

    def maketree(self,e,left,right):
        self.root = Node(e,left.root,right.root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)

    def preorder(self,troot):
        if troot:
            print(troot.element,end=" ")
            self.preorder(troot.left)
            self.preorder(troot.right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element,end=" ")


x=BinaryTree()
y=BinaryTree()
z=BinaryTree()
a=BinaryTree()

x.maketree(20,a,a)
y.maketree(30,a,a)
z.maketree(10,x,y)
print("inorder traversal")
z.inorder(z.root)
print()
print("preorder")
z.preorder(z.root)
print()
print("postorder traversal")
z.postorder(z.root)