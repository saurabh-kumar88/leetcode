# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return 
        
        nodes = [] # result
        queue = deque([root])
        
        # BFS on tree using queue
        
        while(queue):
            level = len(queue)
            levelNodes = []
            
            for i in range(level):
                currentNode = queue.popleft()
                levelNodes.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                
            nodes.append(levelNodes)
        
        nodes.reverse()
        return nodes