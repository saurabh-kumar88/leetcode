class Solution:
  def reverseWords(self, s: str) -> str:
      
    # remove leading/trailing space 
    s = s.strip()
    # remove multiple white spaces in between words
    string = re.sub("\s\s+", " ", s)
    char_arr = string.split(" ")
    ans = ""
    for word in char_arr[::-1]:
        ans += word + " "
    return ans.rstrip()

if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseWords("foo bar"))
        