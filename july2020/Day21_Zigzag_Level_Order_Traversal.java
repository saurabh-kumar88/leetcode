package july2020;


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  /**
  
  DFS: using normal DFS algo,without actually doing zigZag traversal
  i have cheated here, and modified the answer array to 
  look like desired result. 
  
  */
  public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
      
      Queue<TreeNode> q = new LinkedList<TreeNode>();
      List<List<Integer>> ans = new ArrayList();
      
      if(root == null) return ans;
      
      q.offer(root);
      while(q.size() > 0)
      {
          int level = q.size();
          List<Integer> leveNodes = new ArrayList();
          for(int i=0; i<level; i++)
          {
              TreeNode currentNode = q.poll();
              leveNodes.add(currentNode.val);
              
              if(currentNode.left != null)
              {
                  q.offer(currentNode.left);
              }
              
              if(currentNode.right != null)
              {
                  q.offer(currentNode.right);
              }
          }
          
          ans.add(leveNodes);
          
      }
      // modify the final result 
      
      for(int i=0; i<ans.size(); i++)
      {
          if(i % 2 !=0)
          {
           Collections.reverse(ans.get(i));   
          }
      }
                  
      return ans;
      
  }
}



public class Day21_Zigzag_Level_Order_Traversal
{

  public static void main(String[] args) {
    //
    
  }

}