from itertools import permutations
class Solution:
	def getPermutation(self, n: int, k: int) -> str:
	    
	    perm = list(  permutations([x for x in range(1,n+1)])  )     
	    ans = ""
	    for i in perm[k-1]:
	        ans += str(i)
	    return ans
            
        
        