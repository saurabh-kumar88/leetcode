import re
class Solution:
    def toGoatLatin(self, S: str) -> str:
        # 1st rule : if starts with vowel (a, e, i, o, or u), append 'ma' to end
        # 2nd rule : if starts with consonent(non vowel), remove first letter and append it last, then append 'ma' at end
        # 3rd rule : add letter 'a' at the end, depending on index of words, starting with 1
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        charArray = S.split(" ")
        for word in range(len(charArray)):
            # print(charArray[word], " ",charArray[word][0] )
            if charArray[word][0] in vowel:
                charArray[word] += "ma" + ( (word + 1) * "a")
            else:
                temp = list(charArray[word])
                x = temp.pop(0)
                temp.append(x)
                charArray[word] = "".join(temp)
                charArray[word] += "ma" + ( (word + 1) * "a")
            
        ans = " ".join(charArray)
        
        return ans.strip()

if __name__ == '__main__':
    obj = Solution()
    print(obj.toGoatLatin("I speak Goat Latin"))