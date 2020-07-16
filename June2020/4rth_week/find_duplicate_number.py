class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # sliding window algorithm
        p1 = 0
        p2 = p1 + 1
        i = 0
        while(i<n):
            if p1 == n:
                break 
            elif(nums[p1]^nums[p2] == 0):
                return nums[p1]
            i += 1
            p1 = i
            p2 = p1+1
        