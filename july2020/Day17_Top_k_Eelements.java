package july2020;
class Solution {
  public int[] topKFrequent(int[] nums, int k) {
   
      // 1.  map frequency
      Map<Integer, Integer> map = new HashMap();
      for(int n : nums)
      {
        // shortcut method to count freq.
          
          map.put(n, map.getOrDefault(n,0) + 1); 
          // map.getOrDefault(key, value) --> if key present, it will return value assigned to it, or it will return default                  value provided i.e 0
          
      }
      
      // init heap 'the less frequent element first'
      Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> map.get(n1) - map.get(n2) );
      
      // 2. keep K top frequent elements in the heap
      for(int n : map.keySet())
      {
        heap.add(n);
          if(heap.size() > k) heap.poll();
      }
      // 3. Prepare output array
      int[] ans = new int[k];
      
      for(int i=k-1; i >= 0; --i )
      {
          ans[i] = heap.poll();
      }
      
      return ans;
  }
}

public class Day17_Top_k_Eelements{


    public static void main(String[] args) {
      Solution obj = new Solution();
      System.out.println(obj.topKFrequent([1,1,1,2,2,3], 2));
    }


}

