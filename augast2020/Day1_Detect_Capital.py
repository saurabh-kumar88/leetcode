import re
class Solution:
  """
  1. check if all letters are in UPPER CASE
  2. or check if all letters are in LOWER CASE
  3. or check first letter in UPPER CASE then rest should be in UPPER CASE
  4. return False if there is a white space in between letters
  """
  def detectCapitalUse(self, word: str) -> bool:

    if self.all_UPPERCASE(word):
      return True
    elif self.all_LOWERCASE(word):
      return True
    elif self.is_Camel_Case(word):
      return True
    else:
      return False
    
  # 1. helper methods  
  def all_UPPERCASE(self, word_string: str) -> bool:

    upper_case = re.findall("[A-Z]", word_string)
    if len(word_string) == len(upper_case):
      return True
    else:
      return False

  # 2. helper methods
  def all_LOWERCASE(self, word_string: str) -> bool:

    lower_case = re.findall("[a-z]", word_string)
    if len(word_string) == len(lower_case):
      return True
    else:
      return False
  # 3. helper methods
  def is_Camel_Case(self, word_string: str) -> bool:
    first_letter = re.findall("[A-Z]", word_string[0])
    
    if len(first_letter) == 1:
      upper_case = re.findall("[a-z]", word_string)
      print("upper_case ", len(upper_case), "word_string ", len(word_string))
      if len(upper_case) == len(word_string)-1:
        return True
      else:
        return False




if __name__ == '__main__':
  obj = Solution()
  print(obj.detectCapitalUse("Leetcode"))

                           