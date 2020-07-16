class Solution:
      
  def prisonAfterNDays(self, cells, N):
    """
    :type cells: List[int]
    :type N: int
    :rtype: List[int]
    """
    
    if N > 14:
        N = N%14

    if N%14 == 0:
        N = 14
    
    for i in range(1, N+1):
        temp = [0]*len(cells)
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                temp[i] = 1
            else:
                temp[i] = 0
        cells = temp
    return(cells)            

# driver code
cells = [0,1,0,1,1,0,0,1]
N = 7
if __name__ == "__main__":
  obj = Solution()
  print(obj.prisonAfterNDays(cells, N)) 
  


            