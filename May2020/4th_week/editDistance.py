from collections import Counter
class Solution:
  COUNT = 0
  def minDistance(self, word1, word2) -> int:
    
    n = len(word1)
    m = len(word2)
    w1 = self.string_to_list(word1)
    w2 = self.string_to_list(word2)
    
    # corner case

    if (n == 0) and m >0:
      return m
    elif (m == 0) and n >0:
      return n

    return Solution.COUNT
      
  def string_to_list(self,string):
    result = []
    for letter in string:
      result.append(letter)
    return result
  
  def list_to_string(self, List):
    string= ""
    for element in List:
      string += "".join(element)
    return string

  
  def update_counter(self):
    Solution.COUNT += 1


word1 = "intention"
word2 = "execution"

# word1 = "horse"
# word2 = "ros"

# word1 = ""
# word2 = "a"

# word1 = "a"
# word2 = "b"

# word1 = "a"
# word2 = "ab"

# word1 = "a"
# word2 = "a"

if __name__ == "__main__":
  obj = Solution()
  # print(obj.minDistance(word1, word2))

  x = Counter(word1)
  y = Counter(word2)
  print(x)
  print(y) 


  




    
    

