package july2020;

class Solution {
  public String reverseWords(String s) {
      String ans = "";
      String after = s.trim().replaceAll(" +", " "); // remove leading/trailing and multiple spaces between words
      
      String[] arr = after.split(" ");
      int n = arr.length -1;
      
      while(n != -1)
      {
          ans = ans + arr[n] + " ";
          n--;
      }
      return ans.trim();       
  }
}


public class Day15_reverse_words_in_string{

  public static void main(String[] args) {
    Solution obj = new Solution();
    System.out.println(obj.reverseWords("  foo bar !"));
  }

}