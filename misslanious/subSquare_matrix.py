"Given a m * n matrix of ones and zeros, return how many square submatrices have all ones."

# -------- Algorithm ----------
# step1: all non zeros = sub-square matrix [1x1]

# Note1:: mat = m x n, sub-square matrix k x k where k <= m, k<=n (but here might be m != n)

# Note2:: e.g here mat = 3x4 so,sub-square can be of [3x3], [2x2] and [1x1]

# Note3:: i.e sub-square is raw dependent

# step2: loop through mat, and create sub-square matrix

# step3: calculate sum of every sun-square, 
# if sum of sub-square is same as expected then it will be valid subsquare otherwise not

# Note:: sum of sub-square = row x col (for matrix of all 1's only)

# mat = [[0, 1, 1, 1], 
#        [1, 1, 1, 1], 
#        [0, 1, 1, 1],]


import numpy as np

class Solution:
  def countSquares(self, matrix ) -> int:
    
    sub_square = 0
    n = len(mat)
    k = 1 # sub-matrix diemention-> increment k up to n
    
    for i in range(n-1):
      for j in range(n-1):   
        print( mat[i][j], end=" " )
      print()              
            
                    
    
    




mat = [[0, 1, 1, 1], 
       [1, 1, 1, 1], 
       [0, 1, 1, 1],] 



if __name__ == "__main__":
    obj = Solution()
    print( obj.countSquares(matrix=mat) )
    
    
    




