class Solution:
  def searchInsert(self, nums, target) -> int:
    # check if target present in array
    # if target in nums:
    #   return nums.index(target)
    # else:
    #   return self.searchPosition(nums, target)
    return self.searchInsert2(nums, target)
          
  # helper method to search appropriate position
  def searchPosition(self, arr, sub):
    index = 0
    while index < len(arr):
      if arr[index] < sub:
        pass
      elif arr[index] > sub:
        return index  
      index += 1
    return len(arr)
  
  def searchInsert2(self, nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
      if l == r:
        if target <= nums[l]:
          return l
        else:
          return l+1
      mid = (l+r) >> 1
      
      if nums[mid] > target:
        r = mid 
      elif nums[mid] < target:
        l = mid + 1 
      else:
        return mid

        


# driver code

if 0:
  num = [1,3,5,6]
  target = 5
  # o/p : 2

if 0:
  num = [1,3,5,6]
  target = 2
  # o/p : 1

if 0:
  num = [1,3,5,6]
  target = 7
  # o/p : 4

if 0:
  num = [1,3,5,6]
  target = 0
  # o/p : 0

if 0:
  num = [1,2,4,6,9,12]
  target = 15

if 1:
  num = [1]
  target = 0

if __name__ == "__main__":
    obj = Solution()
    print(obj.searchInsert(num, target))

    

         