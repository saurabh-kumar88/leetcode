class Solution:
    def singleNonDuplicate(self, nums) -> int:
    
        # binary-search 
        lo = 0
        hi = len(nums) - 1

        while(lo < hi):

            mid = lo + (hi - lo)//2
            prev_mid = mid
            print("mid", mid)
            print("prev_mid", prev_mid)
            if nums[mid] == nums[mid+1]:
                hi = mid-1
            elif nums[mid] == nums[mid-1]:
                lo = mid+1
            elif nums[mid] != prev_mid:
                return nums[mid]
        return -1



arr = [1,1,2,3,3,4,4,8,8]
# arr = [3,3,7,7,10,11,11]
# arr = [1,1,2,3,3,5,5,8,8,11,11]

if __name__ == "__main__":
    obj = Solution()
    print( obj.singleNonDuplicate(arr) )
    
    
     



