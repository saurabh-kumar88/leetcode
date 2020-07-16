package july2020;

class Solution {
  public int arrangeCoins(int n) {
    long left = 0, right = n;
    long k, curr;
    while (left <= right) {
      k = left + (right - left) / 2;
      curr = k * (k + 1) / 2;

      if (curr == n) return (int)k;

      if (n < curr) {
        right = k - 1;
      } else {
        left = k + 1;
      }
    }
    return (int)right;
  }
}

public class Day1_arranging_coins{

    public static void main(String[] args) {
      
      Solution obj = new Solution();
      obj.arrangeCoins(5);


    }

}