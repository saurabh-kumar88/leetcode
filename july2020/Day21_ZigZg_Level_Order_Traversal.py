# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  """
  DFS: using normal DFS algo,without actually doing zigZag traversal
  i have cheated here, and modified the answer array to 
  look like desired result. 
  """
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    
    q = deque([root])
    ans = []

    if(root is None):
      return ans
    
    while(len(q) > 0):
      level = len(q)
      levelNodes = []
        
      for i in range(level):
        currentNode = q.popleft()
        levelNodes.append(currentNode.val)
        
        if(currentNode.left):
          q.append(currentNode.left)
        if(currentNode.right):
          q.append(currentNode.right)
          
      ans.append(levelNodes)
    
    # modify the result array to desired answer
    for i in range(len(ans)):
      if(i % 2 != 0):
        ans[i].reverse()
        
    return ans


if __name__ == "__main__":
    obj = Solution()
    
            
                    
                    
            
            
            
        
    
    
        
        
