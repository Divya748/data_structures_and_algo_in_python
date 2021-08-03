class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head= None
    
    
    def push(self , data):
        """
        This method is used to insert/push the data into the stack
        """
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def is_empty(self):
        """
        This method is used to check whether the stack is empty or not
        """
        return self.head is None

    def pop(self):
        """
        This method is used to delete/pop elements from the stack
        """
        if self.is_empty():
            print("stack is empty")
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
    
    def peek(self):
        """
        This method is used to print top of the element in the stack
        """
        if not self.is_empty():
            return self.head.data
        else:
            print("stack is empty")
    
    
    def traversal(self):
        """
        This method is used to traverse every element in the stack
        """
        a=" "
        temp=self.head
        while temp != None:
            a=a+str(temp.data)+'\t'
            temp=temp.next
        print(a)


object=Stack()
object.push(25)
object.push(250)
object.push(2500)
object.push(25000)

object.traversal()