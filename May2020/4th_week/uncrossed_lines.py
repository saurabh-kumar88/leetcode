import copy
class Solution:
  def maxUncrossedLines(self, A, B ) -> int:

    n = len(A)
    m = len(B)
    arr_dict = {}
    arr_dict[n] = A
    arr_dict[m] = B

    temp = [x for x in range(2)]
    arr = []
    
    if len(A) == len(B):
      X = A
      Y = B
    else:
      X = min(arr_dict[n], arr_dict[m])
      Y = max(arr_dict[n], arr_dict[m])
    
    
    for i in range(len(Y)):
      for j in range(len(X)):
        if Y[i] == X[j]:
          temp[0] = j
          temp[1] = i
          x = copy.copy(temp)
          arr.append(x)

    # print("X ", X)
    # print("Y ", Y)

    # i,j = 0,0
    # z = 0
    # l = 0
    # while i < len(Y):
    #   while j < len(X):
    #     if Y[i] == X[j]:
    #       z += 1
    #       del X[0:j]
    #       break
    #     j += 1
    #   i += 1
    # print(z)
          

    
    print("arr ", arr)
    if len(arr) == 0:
      return 0

    firstUncrossed = arr[0]
    maxUncrossed = 1

    i = 1
    while i < len(arr):
      
      if arr[i][0] > firstUncrossed[0] and arr[i][1] > firstUncrossed[1]:
        maxUncrossed += 1
        firstUncrossed = arr[i]
        
      i += 1
    
    return maxUncrossed






# def uncrossedLines( arr, firstUncrossed, maxUncrossed, i):
  
#   if i > len(arr)-1:
#     return 0
#   else:
#     if arr[i][0] > firstUncrossed[0] and arr[i][1] > firstUncrossed[1]:
#       firstUncrossed = arr[i]
#       maxUncrossed += 1
#     i += 1
#     uncrossedLines(arr, firstUncrossed, maxUncrossed, i)
  
    
    
Arr =  [[0, 2], [0, 5], [1, 1], [1, 4], [2, 3], [3, 2], [3, 5], [4, 1], [4, 4]]
     

# A = [2,5,1,2,5]
# B = [10,5,2,1,5,2]

A = [1,4,2]
B = [1,2,4]

# A = [1,3,7,1,7,5]
# B = [1,9,2,5,1]

# A = [2,1]
# B = [1,2,1,3,3,2]

# A = [1,1,3,5,3,3,5,5,1,1]
# B = [2,3,2,1,3,5,3,2,2,1]

# A = [3]
# B = [3,3,2]

  


if __name__ == "__main__":
    obj = Solution()
    print( obj.maxUncrossedLines(A,B) )
    # print( uncrossedLines(Arr, Arr[0],0,0) )

    
  
    
    


    
  

    


    
     


