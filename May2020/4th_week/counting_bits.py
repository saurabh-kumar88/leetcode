import re
class Solution:
  def countBits(self, num):
    count = []
    temp = None
    for i in range(0,num+1):  
      count.append(len(re.findall('1', "{0:b}".format(i)) ))
    return count

      
if __name__ == "__main__":
    n = 5
    obj = Solution()
    print(obj.countBits(n))

