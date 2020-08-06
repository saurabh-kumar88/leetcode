class Solution {
  public boolean isPowerOfFour(int num) {
      
//         if(num == 2) 
//         {
//           return false;
//         }
      
//         int count = 0;
//         while(num > 0)
//         {
//           num = num & (num -1 );
//           count++;
//         }
      
//         if(count == 1 && (num & 0xAAAAAAAA) == 0 )
//         {
//           return true;
//         }
      
//         return false;
      
      return num != 0 && ((num&(num-1)) == 0) && (num & 0xAAAAAAAA) == 0; 
  }
}


public class Day4_power_of_4{
  public static void main(String[] args) {
    Solution obj = new Solution();
  }
}