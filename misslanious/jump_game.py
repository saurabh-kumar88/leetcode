class Solution(object):
    def canJump(self, nums ) -> bool:
        
        if len(nums) == 1 and nums[0] == 0:
            return True
        if len(nums) == 1 or len(nums) == 0:
            return False

        jump = nums[1]
        N = len(nums) - 1
        if jump > len(nums[1 : N]):
            return False
        if jump == len(nums[1 : N]):
            return True
            
        return False
        

            
        

arr = [0]

if __name__ == "__main__":
    obj = Solution()
    print( obj.canJump(arr) )
    
    # print(len(arr))
    
    # n = len( arr ) -1
    # print("arr[1]", arr[1])
    # print("len(arr[1 : n])", len(arr[1 : n]) )
    # print( "arr[-1]", arr[-1] )
    # p = []
    # print(len(p))