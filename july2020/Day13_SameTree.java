package july2020;


class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
                
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        
        if(p != null)
        {
          s1.push(p);
        }
        if(q != null)
        {
            s2.push(q);
        }
        
        
        while(!s1.isEmpty() && !s2.isEmpty())
        {
            TreeNode node1 = s1.pop();
            TreeNode node2 = s2.pop();
            
            // System.out.println("node1 " + node1.val + " node2 " + node2.val  );
            
            if(node1.val != node2.val )
            {
                return false;
            }
                        
            if(node1.left != null)
            {
             s1.push(node1.left);
            }
            if(node2.left != null)
            {
             s2.add(node2.left);
            }
            if( s1.size() != s2.size())
            {
              return false;
            }
            
            
            if(node1.right != null)
            {
             s1.push(node1.right);
            }
            
            if(node2.right != null)
            {
             s2.push(node2.right);
            }
            
            if( s1.size() != s2.size())
            {
              return false;
            }
            
        }
        
        // default return
        return s1.size() == s2.size();
    }
        
}



public class Day13_SameTree{

	public static void main(String[] args) {
		Solution obj = new Solution();
		obj.isSameTree();
	}

}