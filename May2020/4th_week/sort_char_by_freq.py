"Sort char of given string in decreasing order by their frequency"
"tree -> eert"
from collections import Counter

class Solution:
  def frequencySort(self, s: str) -> str:
    result = ''
    dic = Counter(s)
    # sorting  they keys based on values in decreasing order
    s = sorted(dic, key=lambda x : dic[x], reverse=True )
    print(s, type(s))
    for char in s:
      result += char * dic[char]
    
    return result
    

    
if __name__ == "__main__":
    obj = Solution()
    print(obj.frequencySort("tree"))


