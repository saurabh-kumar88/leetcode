class Day6_plusOne:
  """
  An array is given called digits, a non negative
  integer is represented by its elements, return 
  this integer + 1 as collection of array elements
  e.g arr = [1,2,3], o/p [1,2,4]
  """
  def plusOne(self, digits):
    # numStr = ''.join([str(x) for x in digits])
    # Integer = str(int(numStr) + 1)
    # ans = [int(z) for z in Integer]            
    # return ans
    
    n = len(digits)
    right_most = digits[0]
    for i in reversed(range(n)):
      if(digits[i] != 9):
          digits[i] += 1
          break
      else:
          digits[i] = 0
    
    if digits[0] == 0:
      digits.insert(0, 1)
        
    return digits

if __name__ == "__main__":
    obj = Day6_plusOne()
    print(obj.plusOne([9,9]))

                
        
            
        