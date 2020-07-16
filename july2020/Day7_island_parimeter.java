class Solution {
  public int islandPerimeter(int[][] grid) {
      int parimeter = 0;
      int R = grid.length;  
      int C = grid[0].length;
      
      for(int x=0; x<R; x++)
      {
          for(int y=0; y<C; y++ )
          {
              if( grid[x][y] == 1)
              {
                if(x == 0 || grid[x-1][y] == 0)
                {
                  parimeter++;  
                }
                if(x == R-1 || grid[x+1][y] == 0)
                {
                  parimeter++;  
                }
                if(y == 0 || grid[x][y-1] == 0)
                {
                  parimeter++;  
                }
                if(y == C-1 || grid[x][y+1] == 0)
                {
                  parimeter++;  
                }
                             
              }
          }
      }
      return parimeter;
      
  }
}

public class Day7_island_parimeter
{

  public static void main(String[] args) {
    
    int[][] grid = {{0,1,0,0}, {1,1,1,0}, {0,1,0,0}, {1,1,0,0}}; 

    // expected o/p : 16
    Solution obj = new Solution();
    System.out.println(obj.islandPerimeter(grid));

  }



}

