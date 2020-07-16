from collections import deque
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def bstFromPreorder(self, preorder):
    "itype  preorder : list"
    "rtype root node : root"
    # node.val --> node.left --> node.right

    r = TreeNode(preorder[0])
    for elem in preorder:
      self.insert(r, TreeNode(elem) )

    self.traverse_preorder(r)
  

  def insert(self, root, node):
    if root is None:
      root = node
    else:
      if root.val < node.val:
        if root.left is None:
          root.left = node
          # root.right = None
          self.insert(root.left, node)
      elif root.val > node.val:
        if root.right is None:
          root.right = node
          # root.left = None
          self.insert(root.right, node)
        
          

  
  def traverse_preorder(self,root):
    
    if root:
      print(root.val,"-->",end=" ")
      self.traverse_preorder(root.left)
      self.traverse_preorder(root.right)
      
      
  
    

arr = [8,5,1,7,10,12]



# Output: [8,5,10,1,7,null,12]

if __name__ == "__main__":
    
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.right = TreeNode(10)
    
    obj = Solution()
    # obj.bstFromPreorder(arr)
    obj.traverse_preorder(root)
   
    
    
    
      





    