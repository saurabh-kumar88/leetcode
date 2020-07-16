# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    arr = self.inorder_traversal(root)
    return arr[k-1]
      
  # Helper method inorder_traversal (Note: inorder traversal sort bst in increasing order)
  def inorder_traversal(self, root):
    elements = []
    
    if root:
      elements += self.inorder_traversal(root.left)
      elements.append(root.val)
      elements += self.inorder_traversal(root.right)
    
    return elements
        