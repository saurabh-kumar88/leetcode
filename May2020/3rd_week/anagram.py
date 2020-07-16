
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
      
      "rtype s : str"
      "rtype p : str"
      "ptype List: list"
      "Algorithm : sliding window"

      n = len(s)
      k = len(p)
      # base case
      if k > n:
        return -1
      
      List = []
      
      p_count = Counter(p)
      s_count = Counter(s[:k])
      
      i = 0
      while i < (n - k):
        if s_count == p_count:
          List.append(i)
        next_char = s[i + k]
        # check if next_char exists in s_count
        if next_char in s_count:
          s_count[next_char] += 1
        else:
          s_count[next_char] = 1
        
        # print( s_count )
              
        s_count[s[i]] -= 1
        if s_count[s[i]] == 0:
          del s_count[s[i]]
        i += 1
      if s_count == p_count:
        List.append(i)
        
      return List

           
s = "cbaebabacd"
p = "abc"


if __name__ == "__main__":
  obj = Solution()
  print( obj.findAnagrams(s, p) )
  
  # c1, c2 = Counter(p), Counter(s[:len(p)])
  # print(c1,c2)




