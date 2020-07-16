# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def searchBST(self, root: TreeNode, val: int) -> TreeNode:  
    if root is None or root.val == val:
      return root
    else:
      if root.val > val :
        if root.left:
          return self.searchBST(root.left, val)
      if root.val < val :
        if root.right:
          return self.searchBST(root.right, val)
        