package july2020;

class Solution {
  public int nthUglyNumber(int n) {
   
      
      // step1: initialize empty array of size n 
      int[] ugly = new int[n];
      
      // step2: 1 is ugly numebr, initialize arrays first number equals to 1
      ugly[0] = 1;
      
      //step3 : initialize 3 index variables which points to first element of array 
      int i2=0, i3=0, i5=0;
      
      // step4: Initialize 3 choices for next ugly number
      int next_multiple_i2 = ugly[i2]*2;
      int next_multiple_i3 = ugly[i3]*3;
      int next_multiple_i5 = ugly[i5]*5;
      
      // step5: search all ugly numbers upto n and fill in ugly[] 
      // algorithm - merge sort
      for(int i=1; i<n; i++)
      {
          int next_ugly = Math.min(next_multiple_i2, Math.min(next_multiple_i3, next_multiple_i5) );
      
          // step6: adding new uglyl number to array
          ugly[i] = next_ugly;
          
          if(next_ugly == next_multiple_i2)
          {
              i2 = i2 + 1; // increment index pointer
              next_multiple_i2 = ugly[i2]*2; // increment multiple of i2
          }
          
          if(next_ugly == next_multiple_i3)
          {
              i3 = i3 + 1;
              next_multiple_i3 = ugly[i3]*3;
          }
          
          if(next_ugly == next_multiple_i5)
          {
              i5 = i5 + 1;
              next_multiple_i5 = ugly[i5]*5;
          }
      
      }
      
      return ugly[n-1];
  }
}




public class Day4_isUgly_number2{

    public static void main(String[] args) {
      
      Solution obj = new Solution();
      System.out.println( obj.nthUglyNumber(10)); 

    }



}