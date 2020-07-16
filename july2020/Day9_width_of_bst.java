package july2020;
import java.util.*;
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

/*
We know that a binary tree can be represented by an array (assume the root begins from the position with index 1 in the array). If the index of a node is i, the indices of its two children are 2*i and 2*i + 1. The idea is to use two arrays (start[] and end[]) to record the the indices of the leftmost node and rightmost node in each level, respectively. For each level of the tree, the width is end[level] - start[level] + 1. Then, we just need to find the maximum width.
*/


class Solution {
  public int widthOfBinaryTree(TreeNode root) {
      return dfs(root, 0, 1, new ArrayList<Integer>(), new ArrayList<Integer>());
  }
  
  public int dfs(TreeNode root, int level, int order, List<Integer> start, List<Integer> end){
      if(root == null)return 0;
      if(start.size() == level){
          start.add(order); end.add(order);
      }
      else end.set(level, order);
      int cur = end.get(level) - start.get(level) + 1;
      int left = dfs(root.left, level + 1, 2*order, start, end);
      int right = dfs(root.right, level + 1, 2*order + 1, start, end);
      return Math.max(cur, Math.max(left, right));
  }
}

public class Day7_width_of_bst
{
    public static void main(String[] args) {
      Solution obj = new Solution();
      obj.widthOfBinaryTree(root);
    }

}


