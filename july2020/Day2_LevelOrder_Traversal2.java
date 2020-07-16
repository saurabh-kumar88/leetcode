package july2020;

import java.util.*;

class Solution {
  public List<List<Integer>> levelOrderBottom(TreeNode root) {
      
      ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
      
      // base case
      if(root == null)
      {
        return res;
      }
      
      ArrayList<Integer> nodes = new ArrayList<Integer>();
      Queue<TreeNode> q = new LinkedList<TreeNode>();
      
      q.offer(root);
      
      while(!q.isEmpty())
      {
          int level = q.size();
          ArrayList<Integer> levelNodes = new ArrayList<Integer>();
          
          for(int i=0; i<level; i++)
          {
              TreeNode currentNode = q.poll();
              
              levelNodes.add(currentNode.val);
              
              if(currentNode.left != null)
                  q.offer(currentNode.left);
              if(currentNode.right != null)
                  q.offer(currentNode.right );        
              
          }
          
          res.add(levelNodes);
          
      }
      
      Collections.reverse(res);
      return res;   
      
  }
}


public class Day2_LevelOrder_Traversal2{

    public static void main(String[] args) {
      Solution obj = new Solution();
      obj.levelOrderBottom(root); 
    }



}