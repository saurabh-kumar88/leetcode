class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
      if n == 0:
        return False
      while(n != 1):
        if(n%2 != 0):
            return False
        n = n//2
      return True

# ____________ Another method ______________
# power of 2 ,4 , 8 numbers have only bit set in their bit-map
import re
def isPowerOfTwo_bitMap(n):
  if n < 0:
    return False
  bitMap = '{0:b}'.format(n)
  count_1s = len(re.findall('1', bitMap))
  return True if count_1s == 1 else False


num = 256
if __name__ == "__main__":
    obj = Solution()
    obj.isPowerOfTwo(num)
    