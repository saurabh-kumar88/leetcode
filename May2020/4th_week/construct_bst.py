# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def bstFromPreorder(self, preorder) -> TreeNode:
    root, i = self.buildTree(min(preorder), max(preorder), 0, preorder)
    return root
  
  def buildTree(self, min_val, max_val, i, preorder):
    if i == len(preorder) or preorder[i] < min_val or preorder[i] > max_val:
        return [None, i]
    val = preorder[i]
    i += 1
    node = TreeNode(val)
    node.left, i = self.buildTree(min_val, val, i, preorder)
    node.right, i = self.buildTree(val, max_val, i, preorder)
    return [node, i]