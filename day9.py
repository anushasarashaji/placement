class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


# traversal
# inorder= l rt r
# postorder= l r rt
# preorder = rt l r

class BST:
    def __init__(self):
        self.root=None

    def insert(self,node,data):

        if node is None:
            return Node(data)
        if data < node.data:

            node.left=self.insert(node.left,data)
        elif data>node.data:
            node.right=self.insert(node.right,data)
        return node
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

tree=BST()
tree.root=tree.insert(tree.root,5)
tree.root=tree.insert(tree.root,3)
tree.root=tree.insert(tree.root,1)
tree.root=tree.insert(tree.root,2)
tree.inorder(tree.root)
