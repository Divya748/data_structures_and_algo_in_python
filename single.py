#single-linked list
class Node:
    def __init__(self,value):
        self.info=value
        self.link=None
class singlell:
    def __init__(self):
        self.start=None
    
    def insert_at_begin(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp

    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
    
    def insert_at_position(self,k,data):
        if k==1:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return 
        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.link
            i+=1
        if p is None:
            print("you can insert value upto position",i)
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp


    def  insert_before_value(self,val,data):
        #if value is in first node,new node is to be inserted at the begining
        if val==self.start.info:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
        #find kink of node prececence of the node containing given value
        p=self.start
        while p.link is not None:
            if p.link.info==val:
                break
            p=p.link
        if p.link is None:
            print(val,"is not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp

    def insert_after_value(self,val,data):
        p=self.start
        while p is not None:
            if p.info==val:
                break
            p=p.link
        if p is None:
            print(val,"is not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp

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
            return
        else:
            print("list is: ")
            p=self.start
            while p is not None:
                print(p.info)
                p=p.link
            print()
if __name__ == "__main__": 
    single_list= singlell()
    single_list.create_list()
    print('''
        1.Display the list
        2.Insertion at begining
        3.Insertion at end
        4.Insert a node after given value
        5.Insert a node before given value
        6.Insert a node at given position
        ''')
    i=int(input("enter your choice from the above menu: "))
    if i==1:
        single_list.display_list()
    elif i==2:
        data=int(input("enter the data"))
        single_list.insert_at_begin(data)
        single_list.display_list()
    elif i==3:
        data=int(input("enter the data"))
        single_list.insert_at_end(data)
        single_list.display_list()
    elif i==4:
        val=int(input("enter the value"))
        data=int(input("enter the data"))
        single_list.insert_after_value(val,data)
        single_list.display_list()
    elif i==5:
        val=int(input("enter the value"))
        data=int(input("enter the data"))
        single_list.insert_before_value(val,data)
        single_list.display_list()
    elif i==6:
        val=int(input("enter the position"))
        data=int(input("enter the data"))
        single_list.insert_at_position(val,data)
        single_list.display_list()
    else:
        print("enter the correct option")
        