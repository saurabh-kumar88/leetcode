class Solution(object):
    MAX_INT = 2**31 -1
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        while temp:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num
        
        
if __name__ == "__main__":
    obj = Solution()
    print( obj.findComplement(5) )
   
 
    