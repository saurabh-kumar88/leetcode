class Solution {
    public int longestPalindrome(String s) {
        
        int ans = 0;
        int sum_of_evens = 0;
        int sum_of_odds = 0;
        boolean is_odd_count = false;
        int conditional_one = 0;
        
        HashMap<Character, Integer> freq = new HashMap();
        
        char[] arr = s.toCharArray();
        
        // Count characters freq
        for(int i=0; i<arr.length; i++  )
        {
          if(freq.containsKey(arr[i]) )
          {
              freq.put(arr[i], freq.get(arr[i]) + 1 );
          }
            else
            {
                freq.put(arr[i] , 1);
            }
        }
        
        for(Character _key : freq.keySet() )
        {
            if(freq.get(_key) % 2 == 0)
            {
                sum_of_evens += freq.get(_key);
            }
            
            if(freq.get(_key) % 2 != 0)
            {
                sum_of_odds += freq.get(_key) -1;
                is_odd_count = true;
            }
        }
        
        if(is_odd_count)
        {
            conditional_one = 1;
        }
        
        ans = sum_of_evens + sum_of_odds + conditional_one;
        return ans;
        
        
    }
}


class public Day14_Longest_palindrome{


    public static void main(String[] args) {
        Solution obj = new Solution();
    }
}