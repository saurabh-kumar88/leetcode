import operator
from collections import Counter, OrderedDict
class Solution:
  def topKFrequent(self, nums, k):
    freq = Counter(nums)
    ans = []
    freq_values = sorted(freq.values())
    
    count = 0
    while count < k:
      for key in sorted(freq.keys(), reverse=False):
        print(" key " , key, " value ", value)
        ans.append(key)
        k -= 1
    
     
    print(ans[0:k])
    return ans[0:k]

def testFunc(arr):
  x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
  sorted_x = sorted(x.items(), key=operator.itemgetter(0))


# driver code
arr = [4,4,4,4,1,-1,2,-1,2,3]
K = 2


if __name__ == "__main__":
    obj = Solution()
    # print( obj.topKFrequent(arr, K) )
    print( testFunc(arr) )
            
            