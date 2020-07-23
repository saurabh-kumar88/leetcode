from collections import Counter
class Solution:    
  def singleNumber(self, nums):
    freq = Counter(nums)
    ans = []
    for key in freq.keys():
      if freq[key] == 1:
        ans.append(key)
    return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNumber([1,6,4,1,3,5,6]))

    