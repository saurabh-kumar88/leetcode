package july2020;

/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
  public Node flatten(Node head) {
      Node temp = head;
      Stack<Node> stk = new Stack<>();
      while(head != null){
          if(head.child != null){
              if(head.next != null)
              {
               stk.push(head.next);
              }
              head.next = head.child;
              head.next.prev = head;
              head.child = null;
          }
          else if(head.next == null && !stk.isEmpty()){
              head.next = stk.pop();
              head.next.prev = head;
          }
          head = head.next;
      } 
    return temp;
  }
}

public class Day10_flatten_doubly_linkedlist{

    public static void main(String[] args) {
      //
    }

}
