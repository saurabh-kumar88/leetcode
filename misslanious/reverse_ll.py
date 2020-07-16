# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    

    def print_ll(self, head):
        current = head
        while( current  ):
            print(current.val)
            current = current.next

    def reverseList(self, head):
        "_______Iterative Approach_______"

        "To reverse a singly linked list, we have to use 3 pointer"
        "previous : initially set to None , which holds address of previous node "
        "current : hold address of current node "
        "following : holds address of current.next"

        "Step1 : intially declare all pointers "
        "Step2 : traverse linked list while current is not None"
        # Connection menupilation
        "Step3 : break old connection of current node, previous --> current"
        # Before breaking we have following pointer which holds address of next node 
        "Step4 : Jump current --> following"
        "Step5 : If we have'nt reached to last node then Jump following --> following.next"
        "Step6 : Repeat until last node and in the end set new head"

        previous = None
        current = head
        following = current.next

        while current:
            current.next = previous # breaking the old link
            previous = current # shifting prev from None to last element
            current = following
            if following: # if this is was not last element
                following = following.next #  move to next element
        head = previous
        self.print_ll(head)

    def reverseList2(self, head):
        if head is None:
            return
        self._recursive_reverse( head, None)
        self.print_ll(head)
    

    def _recursive_reverse(self, current, previous):
        
        if current.next is None: # if last node reached
            self.head = current
            current.next = previous
            return
        
        next = current.next
        current.next = previous

        self._recursive_reverse( next, current )
        
        
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




    



        
arr = [5, 4, 3, 2, 1]

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    obj = Solution()
    # result = obj.reverseList(node1)
    # obj.reverseList(node1)
    # obj.reverseList2( node1 )
    # obj.print_ll(node1)


    obj2 = Int_LinkedList()
    obj2.add(ListNode('one' ))
    obj2.add(ListNode('two'))
    obj2.add(ListNode('three'))
    obj2.add(ListNode('four'))
    obj2.print_ll()

    

    












    