
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str)->bool:
      
      "rtype s1 : str"
      "rtype p2 : str"
      "True or False: bool"
      
      k = len(s1)
      n = len(s2)
      
      # base case
      
      
      s1_count = Counter(s1)
      s2_count = Counter(s2[:k])
      # print(s1_count, s2_count)      
      i = 0
      while i < (n - k):
        
        if s1_count == s2_count:
          return True
        
        next_char = s2[i + k]
        # check if next_char exists in s_count
        if next_char in s2_count:
          s2_count[next_char] += 1
        else:
          s2_count[next_char] = 1
                    
        s2_count[s2[i]] -= 1
        if s2_count[s2[i]] == 0:
          del s2_count[s2[i]]
        
        i += 1
      if s1_count == s2_count:
        return True
        
      return False

           
s1 = "ab"
s2 = "a"


if __name__ == "__main__":
  obj = Solution()
  print( obj.checkInclusion(s1, s2) )
  
  