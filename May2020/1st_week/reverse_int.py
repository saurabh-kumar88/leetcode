class Solution:
    def reverse(self, x: int) -> int:
        # check if number is greater then 32 bit
        if x < -(2**31) or x > (2**31) -1:
            return 0
        string = str(x)
        if x < 0:
            result = int("-" + str(-x)[::-1])
        else:
            result = int(string[::-1])
        # Again check 32 bit limit for reversed number
        if result < -(2**31) or result > (2**31) -1:
            return 0
        else:
            return result
        

string = "-123"

if __name__ == "__main__":
    obj = Solution()
    z = obj.reverse(1534236469)
    print(z)
     