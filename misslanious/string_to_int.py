import re

class Solution():
    
    INT_MAX =  (2**31) - 1
    INT_MIN = -(2**31)
    find_digits_only = re.compile(r"^(\s+)?([-+]?\d+)")
    
    def myAtoi(self, input_string: str) -> int:
        "Description : convert strign to integer"
        number = self.find_digits_only.search( input_string )
        
        if number:
            number = int(number.group())
        
        "check 32-bit limit"
        if number < self.INT_MIN:
            return self.INT_MIN
        elif number > self.INT_MAX:
            return self.INT_MAX
        else:
            return number


if __name__ == "__main__":
    obj = Solution()
    print( obj.myAtoi("  -45") )