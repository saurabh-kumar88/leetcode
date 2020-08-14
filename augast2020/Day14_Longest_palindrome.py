class Solution:
    def longestPalindrome(self, s: str) -> int:
        
    freq = Counter(s)
    
    sum_Of_even = 0
    sum_Of_odd = 0
    isOdd = False
    conditional_one = 0
    for i in freq:
        if freq[i] % 2 == 0:
            sum_Of_even += freq[i]
            
        if freq[i] % 2 != 0:
            sum_Of_odd += freq[i] - 1
            isOdd = True
    if isOdd:
        conditional_one = 1
    ans = sum_Of_even + sum_Of_odd + conditional_one
    return ans


        