"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
  def flatten(self, head):
    if not head: return head
    stack = []
    temp = head # preserve head node
    while(head != None):
      if(head.child != None):
        if(head.next != None) : stack.append(head.next) # save rest of the list
        head.next = head.child
        head.next.prev = head # setting up new head node
        head.child = None
      elif (head.next == None and len(stack)!=0):
        head.next = stack.pop()
        head.next.prev = head
        
        head = head.next
    
    return temp
                
        
        








