import copy
class Solution:
    def intervalIntersection(self, A , B ):
      "type : A List[List[int]]"
      "type : B List[List[int]]"
      "rtype : List[List[int]]"

      temp2 = self.combine_arrays(A, B)
      result = []

      non_common = [z for z in range(2)]
      _common_elem = [z for z in range(2)]
      
      i = 0
      while i < len(temp2):
        
        # calculating mid 
        lo = 0
        hi = len(temp2[i])
        mid = lo + (hi - lo)//2
        non_common[0] = temp2[i][mid]
        non_common[1] = temp2[i][mid -1]
        non_common.sort()
        x = copy.copy(non_common)
        result.append(x)
        
        if i+1 >= len(temp2):
          break
        else:
          set_1 = set(temp2[i])
          set_2 = set(temp2[i+1])
          common = list(set_1 & set_2)
          if len( common ):
            for k in common:
              _common_elem[0] = k
              _common_elem[1] = k
            y = copy.copy(_common_elem)
            result.append(y)
      
        i += 1
      
      return result

  
    # helper method
    def combine_arrays(self, a, b):
      n = len(a)
      temp= []
      combinedArray= []

      # combine each array and sort
      for i in range(n):
        for j in range(len(a[i])):
          temp.append(a[i][j])
          temp.append(b[i][j])
        temp.sort()
        x = copy.copy(temp)
        combinedArray.append(x)
        temp.clear()
      return combinedArray
    
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]


if __name__ == "__main__":
  obj = Solution()
  print( obj.intervalIntersection(A, B) )
  

  


    

        










        