import math
import numpy as np
class Solution:
    def reverseBits(self, n):
        bin_str = self.int_to_bin(n)
        print(bin_str)
        print(int(bin_str, 2))
    
    def int_to_bin(self, n):
        bin_str = ""
        while(n > 0):
            bin_str += str(n%2)
            n = n//2
        for i in range(32 - len(bin_str)):
            bin_str += "0"
        return bin_str
    
    def bin_to_int(self, bin_string):
        m = len(bin_string)
        p = m
        index , num = 0, 0
        while(index < m):
            num = num + int(math.pow(2, p-index)) * int(bin_string[index])
            index += 1
        return num


if __name__ == "__main__":
    obj = Solution()
    obj.reverseBits(43261596)
    
    # print(int("101", 2))


    # a = 43261596
    # b = np.uint32(a)
    # print( "{0:b}".format(b) )

    # 964176192
    
    
    # print(bin(43261596))
    
    # 00111001011110000010100101000000
    # 00111001011110000010100100000000         
            
            
            
        
            
            
            
        