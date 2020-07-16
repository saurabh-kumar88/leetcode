package july2020;

// class Solution {
//   public int[] plusOne(int[] digits) {
      
//     for (int i = digits.length - 1; i >=0; i--) {
//       if (digits[i] != 9) {
//           digits[i]++;
//           break;
//       } else {
//           digits[i] = 0;
//       }
//   }
//   if (digits[0] == 0) {
//       int[] res = new int[digits.length+1];
//       res[0] = 1;
//       return res;
//     }
//     return digits;
//   }

// }

public class Day6_plusOne{


  static int[] plusOne(int[] digits) {
      
    for (int i = digits.length - 1; i >=0; i--) {
      if (digits[i] != 9) {
          digits[i]++;
          break;
      } else {
          digits[i] = 0;
      }
  }
  if (digits[0] == 0) {
      int[] res = new int[digits.length+1];
      res[0] = 1;
      return res;
    }
    return digits;
  }



  public static void main(String[] args) {
    int[] arr = {1,8,9};
    // Solution obj = new Solution();
    // System.out.println(obj.plusOne(arr));
    int[] ans = plusOne(arr);
    for(int i : arr)
      System.out.println(i);

    // System.out.println(plusOne(arr));    
  }


}