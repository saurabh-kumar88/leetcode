import re
import copy

def is_Subsequence(s, t):
  z = 0
  result = ""
  i  = 0
  while i < len(s):
    while z < len(t):
      if s[i] == t[z]:
        result += t[z]
        z += 1
        break
      z += 1
    i += 1
    
  if result == s:
    return True
  else:
    return False

# ____ using iter() ______

def is_Subsequence2(s, t):
  iterOf_t = iter(t)

  for letter in s:
    if letter not in iterOf_t:
      return False
  return True


# _______ using all() function _________
def is_Subsequence3(s, t):
  iterOf_t = iter(t)
  return all(letter in iterOf_t for letter in s)


s = "abc"
t = "cfdfaaaxxaahbgdc"

# s = "axc"
# t = "ahbgdc"

# s = "aaaaaa"
# t = "bbaaaa"


if __name__ == "__main__":
    print( is_Subsequence3(s, t) )
       

    
