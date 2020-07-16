package july2020;


class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
      
      List<List<Integer>> result = new ArrayList<>();
      // step1 : sort the array
      Arrays.sort(nums);
      
      int n = nums.length -1;
      
      for(int i=0; i<n; i++)
      {
        // step2 : declare 3 index variables
          int start = i + 1;
          int end = n;
          
      //  if adjacent elements are same  : to avoid duplicates
          if(i >0 && nums[i] == nums[i-1])
          {
              continue;
          }
          
          while(start < end)
          {
              // if adjacent elements are same : to avoid duplicacy
              if(end<n && nums[end] == nums[end+1])
              {
                  end--;
                  continue;
              }
              
              //case1: sum == 0
              if(nums[i] + nums[start] + nums[end] == 0)
              {
                  List<Integer> triplet = Arrays.asList(nums[i], nums[start], nums[end]);
                  result.add(triplet);
                  start++; // next triplet must be on right side of array
              }
              //case2: sum is negative
              if(nums[i] + nums[start] + nums[end] < 0)
              {
                start++; // next triplet must be on right side of array
              }
              else
              {
                end--; // next triplet must be on left side of array
              }
              
          }
          
      }
      return result;
          
  }
}


// driver code

    public class Day8_3sum
    {
      public static void main(String[] args) {
          int[] arr = {-1, 0, 1, 2, -1, -4};
          // expected 0/p [-1,0,1], [-1,-1,2]
        
          Solution obj = new Solution();
          System.out.println(obj.threeSum(arr));
        
        }
    
    }

