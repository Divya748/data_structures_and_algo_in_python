class Bt:
    def __init__(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None

    def insert_left(self,value):
        if self.lchild == None:
            self.lchild=Bt(value)
        else:
            new_node = Bt(value)
            new_node.lchild=self.lchild
            self.lchild=new_node

    def insert_right(self,value):
        if self.rchild == None:
            self.rchild=Bt(value)
        else:
            new_node = Bt(value)
            new_node.rchild=self.rchild
            self.rchild=new_node
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.value, end=" ")   
        if self.rchild:
            self.rchild.inorder()

root=Bt(None)
root=Bt(6)
root.insert_left(3)
root.inorder()