"Calculate perfect square of positive integer without using any built-in methods"

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while( lo <= hi ):
            mid = lo + (hi - lo)//2
            if num == mid**2:
                return True
            
            if num < mid**2:
                hi = mid - 1
                
            else:
                lo = mid + 1
        return False   

    
if __name__ == "__main__":
    obj = Solution()
    print( obj.isPerfectSquare(36) )
    
    