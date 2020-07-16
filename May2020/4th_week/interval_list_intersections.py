import copy
class Solution:
  def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]'):
    res = []
    a,b = 0,0
    if A and B:
      while a < len(A) and b < len(B):
        lo = max(A[a][0],B[b][0])
        hi = min(A[a][1],B[b][1])
        if lo <= hi :
            res.append([lo,hi])
        if A[a][1] < B[b][1]:
            a+=1
        else:
            b+=1
    return res

    
    
    
    
    
    
    
    