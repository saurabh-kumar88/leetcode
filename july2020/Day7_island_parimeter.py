class Solution:
  def islandPerimeter(self, grid: List[List[int]]):
    R = len(grid)
    C = len(grid[0])
    
    parimeter = 0
    for x in range(R):
      for y in range(C):
        if (grid[x][y] == 1):
          if(x == 0 or grid[x-1][y] == 0):
            parimeter += 1
          if(x == R-1 or grid[x+1][y] == 0):
            parimeter += 1
          if(y == 0 or grid[x][y-1] == 0):
            parimeter += 1
          if(y == C-1 or grid[x][y+1] == 0):
            parimeter += 1
    return parimeter

# drivercode
grid =  [[0,1,0,0],
      [1,1,1,0],
      [0,1,0,0],
      [1,1,0,0]]

 # expected o/p : 16

if __name__ == "__main__":
  obj = Solution()
  print( obj.islandPerimeter(grid) )
      
                        