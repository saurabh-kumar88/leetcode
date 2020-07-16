# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    
    # current = node
    # following = current.next
    
    # current.val = following.val 
    # current.next = following.next

    current, following = node, current.next
    current.val, current.next = following.val, following.next
    
         
        