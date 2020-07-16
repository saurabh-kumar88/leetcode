package july2020;

import java.util.*;
import java.util.regex.*;


class Solution {
  
    

    public int hammingDistance(int x, int y)
    {
        // using built method  
        return Integer.bitCount(x ^ y); 
    }


    public int hammingDistance2(int x, int y)
    {
        // Brian karnighan's algorithm
        int count = 0;
        int n = x ^ y;
        
        while(n > 0)
        {
            n = n & (n-1);
            count++;
        }
        
        return count;
    }
        



}

public class Day5_hammingDistance{

  public static void main(String[] args) {
    
    Solution obj = new Solution();
    System.out.println(obj.hammingDistance(1, 4));
    
  }


}