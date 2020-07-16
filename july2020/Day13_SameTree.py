class Solution:
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    q1 = deque()
    q2 = deque()
    if q is not None:
        q1.appendleft(q)
    
    if p is not None:
        q2.appendleft(p)
     
    while(q1.__len__() and q2.__len__() ):
        
        node1 = q1.pop()
        node2 = q2.pop()
        
        if(node1.val != node2.val):
            return False
        
        if(node1.left):
            q1.appendleft(node1.left)
        
        if(node2.left):
            q2.appendleft(node2.left)
        
        if q1.__len__() != q2.__len__():
            return False
        
        if(node1.right):
            q1.appendleft(node1.right)
        
        if(node2.right):
            q2.appendleft(node2.right)
        
        if q1.__len__() != q2.__len__():
            return False
            
    return q1.__len__() == q2.__len__()

if __name__ == '__main__':
    obj = Solution()
    obj.isSameTree()



