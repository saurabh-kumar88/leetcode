

class Solution {
    public boolean isPalindrome(String s) {
        String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        String rev = new StringBuffer(actual).reverse().toString();
        return actual.equals(rev);
    }
}

public class Day3_valid_palindrome{
  public static void main(String[] args) {
    Solution obj = new Solution();
    

  } 
}