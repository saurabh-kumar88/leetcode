class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in num:
            while stack and stack[-1] > x and k:
                stack.pop()
                k -= 1
            stack.append(x)
            
        return "".join(stack[:len(stack)-k]).lstrip("0") or "0"

if __name__ == "__main__":
    obj = Solution()
    print( obj.removeKdigits("1432219", 3) )
