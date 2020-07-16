# Definition for singly-linked list.
class ListNode:
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

    def hasCycle(self):
        current = self.head
        _mem = {}
        key = 0
        while(current):
            _mem[key] = current
            key += 1
            current = current.next
        
        _mem_ref = 1
        for x in _mem.keys():
            if _mem[1] == _mem[x]:
                _mem_ref += 1
        

        if _mem_ref > 1:
            return True
        return False
            

        

if __name__ == "__main__":
    obj = Linked_List()
    obj.add(ListNode(1))
    obj.add(ListNode(2))
    obj.add(ListNode(3))
    obj.add(ListNode(4))

    # obj.print_ll()
    obj.hasCycle()
