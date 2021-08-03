class Node:
    def __init__(self,value):
        self.info=value
        self.plink=None
        self.alink=None

class doublell:
    def __init__(self):
        self.start=None
    
    def insert_at_end(self,data):
        temp=Node(data)
        if self.start==None:
            temp.plink=None
            self.start=temp
            return
        p=self.start
        while p.alink is not None:
            p=p.alink
        p.alink=temp
        temp.plink=p
    
    def insert_at_begin(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        temp.alink=p
        p.plink=temp
        self.start=temp

    def insert_at_position(self,data,pos):
        temp=Node(data)
        if pos==1:
            temp.alink=self.start
            self.start.plink=temp
            self.start=temp
            return 
        p=self.start
        i=1
        while i<pos-1 and p is not None:
            p=p.alink
            i+=1
        if p is None:
            print("you can insert value upto position",i)
        else:
            temp.alink=p.alink
            temp.plink=p
            p.alink=temp
    def insert_after_value(self,data,val):
        pass
    
    def create_list(self):
        n=int(input("enter the no:of nodes: "))
        if n==0:
            return
        for i in range(n):
            data=int(input("enter the element to be insert"))
            self.insert_at_end(data)

    def display_list(self):
        if self.start is None:
            print("List is empty")
        else:
            print("list is: ")
            p=self.start
            while p is not None:
                print(p.info,"-->",end=" ")
                p=p.alink
    
if __name__ == "__main__":
    double_list=doublell()
    double_list.create_list()
    print('''
        1.Display the list
        2.Insertion at begining
        3.Insertion at end
        4.Insert a node at given position
        5.Insert a node after given value
        6.Insert a node before given value
        7.Deletion at begining
        8.Deletion at ending
        9.delete a value
        ''')
    i=int(input("enter your choice from the above menu: "))
    if i==1:
        double_list.display_list()
    elif i==2:
        data=int(input("enter the data"))
        double_list.insert_at_begin(data)
        double_list.display_list()
    elif i==3:
        data=int(input("enter the data"))
        double_list.insert_at_end(data)
        double_list.display_list()
    elif i==4:
        data=int(input("enter the data"))
        val=int(input("enter the position"))
        double_list.insert_at_position(data,val)
        double_list.display_list()
    
    