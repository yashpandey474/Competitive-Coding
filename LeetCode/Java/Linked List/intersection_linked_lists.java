/*
Given two linked lists sorted in increasing order, create a new linked list representing the intersection of the two linked lists. The new linked list should be made with its own memory
the original lists should not be changed.
Note: The linked list elements are not necessarily distinct.
*/
public class ListNode {
      int val;
      ListNode next;
      ListNode(int x) {
          val = x;
          next = null;
      }
 }

class Solution{
  public static ListNode solution(ListNode l1, ListNode l2){
    ListNode new = null;
    ListNode head = null;
    ListNode current1 = l1; ListNode current2  = l2;

    while(current1!=null && current2 != null){
      if(current1.val < current2.val){
        current1 = current1.next;
        continue;
      }

      if(current2.val < current1.val){
        current2 = current2.next;
        continue;
      }

      if(new == null){
        new = new ListNode(current1.val);
        head = new;
      }
      else{
        new.next =  new ListNode(curretn1.val);
      }
      
    }
    return head;
    
  }
  public static void main(String[] args){
    
  }
}
