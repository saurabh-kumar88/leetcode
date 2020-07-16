"Convert binary to decimal using linked list"
from functools import reduce

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head:
            self.tail.next = data
        else:
            self.head = data
        
        self.tail = data
 
    def print_ll(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next

    def getDecimalValue(self) -> int:
         
        current = self.head
        arr = []
        while(current):
            arr.append( current.val )
            current = current.next
 
        s1=''.join( map(str, arr) )
        print("s1", s1)
        s1=int(s1 ,2)
        return s1
        
        
    
        

        
    
arr = [1,0,1]

if __name__ == "__main__":
    obj = Linked_List()
    # obj.add(Node(1))
    # obj.add(Node(1))
    # obj.add(Node(1))
    # obj.add(Node(1))

    # obj.print_ll()

    for bit in arr:
        obj.add( Node(bit) )
    # obj.print_ll()

    # print( obj.getDecimalValue() )
    
    number = input("enter a number : ")
    try:
        data = int(number, 2)
    except TypeError as err:
        print("Invalid input")