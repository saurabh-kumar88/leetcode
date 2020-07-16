class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Algorithm :  merge-sort (divide and conqure)
    """
    if len(nums) >1:
      mid = len(nums)//2
      L = nums[:mid]
      R = nums[mid:]
      
      self.sortColors(L)
      self.sortColors(R)
      
      i = j = k = 0
      
      while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
          nums[k] = R[j]
          j += 1
        k += 1
          
      while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
      while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1

# driver code
nums = [2,0,2,1,1,0]
# o/p = [0,0,1,1,2,2]

if __name__ == "__main__":
  myObj = Solution()
  myObj.sortColors()
  print(nums)
                
                
        
        
        