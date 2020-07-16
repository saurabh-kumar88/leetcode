import re

string = "3[abc]4[ab]c"
# string = "10[a]"
# string = "2[3[a]b]"


def decopressString(inputString):
  for char in inputString:
    isDigit = re.findall("\d", char)
    if isDigit:
      print("True ", isDigit )


if __name__ == "__main__":
    decopressString(string)



