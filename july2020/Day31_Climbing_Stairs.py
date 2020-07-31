class Solution:
  def climbStairs(self, n: int) -> int:
    # base cases
    # this problem is same as fibonacci sequence
    """
    1 : [1] --> only one way
    2 : [1,1], [2] --> 2 ways in n = 2 steps
    3 : [1,1,1], [1,2], [2,1] --> 3 ways
    4 : --> there will be 5 ways
    """
    
    if(n == 0):
      return 0
    if(n == 1):
      return 1
    if(n == 2):
      return 2
    
    d = {1 : 1, 2 : 2,}
    for i in range(3, n+1):
      curr = d[i-1] + d[i-2]
      d[i] = curr
    
    return d[n]
            
            