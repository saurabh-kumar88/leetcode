def singleNumnerII(nums):
  count = 0
  candidate = None
  for i in range(len(nums)):
    if count == 0:
      candidate = nums[i]
      count += 1
    elif candidate == nums[i]:
      count = 0
    

        
         
  return candidate


# driver code
nums = [2,2,3,2]
# nums = [0,1,0,1,0,1,99]
# nums = [0,0,0,5]
if __name__ == "__main__":
  print( singleNumnerII(nums) )