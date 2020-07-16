from random import random
class Solution:
  def __init__(self, w):
    self.prefix_sum = []
    prefixSum = 0
    for weight in w:
      prefixSum += weight
      self.prefix_sum.append(prefixSum)
    self.total_sum = prefixSum
      
  def pickIndex(self) -> int:
    # Binary search 
    random_num = random() * self.total_sum
    low, high = 0, len(self.prefix_sum)
    while low < high:
      mid = low + (high - low)//2
      if random_num > self.prefix_sum[mid]:
        low = mid +1
      else:
        high = mid
    return low
      
        


# Your Solution object will be instantiated and called as such:
if __name__ == "__main__":    
  obj = Solution(w=[1,3] )
  param_1 = obj.pickIndex()
  print(param_1)