from collections import Counter
class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
      dic = Counter( '{0:b}'.format(x ^ y)  )
      return dic['1']


if __name__ == "__main__":
    obj = Solution()
    print(obj.hammingDistance(1,4))
        