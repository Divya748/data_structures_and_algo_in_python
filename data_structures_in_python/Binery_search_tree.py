class Bst:
    
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        '''
            This method is used to insert data into the tree
        '''
        if self.key == None:
            '''this condition is used to check whether the root node is none, 
            if it is none insert data into the root node '''
            self.key= data
            return
        if self.key == data:
            return
        if data < self.key:
            '''
            this condition is used to check the data is less then root value if 
            it is less it will insert the value in left sub tree of the root node
            '''
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Bst(data)
                
    def search(self,data):
        """
            This method is used to search given data in the tree or not
        """
        if self.key == data:
            print("search found")
            return
        if data < self.key:
            if self.lchild == None:
                print("search not found")
            else:
                self.lchild.search(data)
        else:
            if self.rchild == None:
                print("search not found")
            else:
                self.rchild.search(data)
    """
    Traversal algorithm for tree are three types
    1.Inorder
        a.print left sub tree
        b.print the root node
        c.print right sub tree
    2.Preorder
        a.print the root node
        b.print left sub tree
        c.print right sub tree
    3.Post order
        a.print left subtree
        b.print right sub tree
        c.print the root node
"""
    def preorder(self):
        print(self.key , end =" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")   
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key , end =" ")

    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("data is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("data is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)        
        return self

    def min_node(self):
        while self.lchild:
            self=self.lchild
        print("smallest value is: ",self.key)

    def max_node(self):
        while self.rchild:
            self=self.rchild
        print("maximum value is :",self.key)



root = Bst(None)
list1=[20,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
print("pre-order")
root.preorder()
print("\n")
root.min_node()
print("\n")
root.max_node()


#root.delete(20)
#print("\nafter deletion")
#root.preorder()