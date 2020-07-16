import re

class Solution(object):
    _pattern_find_digits_only = re.compile(r"^(\s+)?([-+]?\d+)")
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = self._pattern_find_digits_only.search(str)
        if result:
            result = int(result.group())
            
            # clipping
            return min(max(result, self.INT_MIN), self.INT_MAX)
            
        return 0

TestCase1 = "42"
TestCase2 = "-42"
TestCase3 = "-4193 with words"
TestCase4 = "words and 987"
TestCase5 = "-91283472332"
TestCase6 = "   i    -45           am saurabh kumar.... 4 57jksadhkhsak@@@ 8 SADS 7 8    "


if __name__ == "__main__":
    obj = Solution()
    # print(obj.myAtoi(TestCase1))
    # print(obj.myAtoi(TestCase2))
    # print(obj.myAtoi(TestCase3))
    # print(obj.myAtoi(TestCase4))
    # print(obj.myAtoi(TestCase5))
    # print(obj.myAtoi(TestCase6))


