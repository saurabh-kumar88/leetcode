class Solution:
  def largestDivisibleSubset(self, nums):
    
    nums.sort()
    # Boundary conditions
    if not nums or len(nums) == 1:
      return nums
    
    List = []
    low = 0
    high = len(nums) - 1
    
    while low < high:
      if(nums[low]%nums[low+1]==0) or (nums[low+1]%nums[low]==0):
        List.append(nums[low])
      elif(nums[low]%nums[low+1]==nums[low]) or (nums[low+1]%nums[low]==nums[low+1]):
        List.append(nums[low])

      low += 1
    
    # if(nums[high]%nums[0]==0) or (nums[0]%nums[high]==0):
    #     List.append(nums[high])
    
    return List


# arr = [1,2,3]
# # o/p : [1,2] or [1,3]

# arr = [1,2,4,8]
# o/p : [1,2,4,8]

# arr = [546,669]
# o/p : [546]

arr = [3,4,16,8]
# o/p : [4,8,16]

import copy

def largest_Divisible_Subset(arr):

  arr.sort()
  temp = []
  sub = []
  
  low = 1
  high = len(arr) - 1  

  for i in range(high):
    for j in range(i):
      temp.append(arr[j])
    
    sub.append(temp)

  
  return sub


if __name__ == "__main__":
    
    obj = Solution()
    # print(obj.largestDivisibleSubset(arr))


    print(largest_Divisible_Subset(arr))
      
    