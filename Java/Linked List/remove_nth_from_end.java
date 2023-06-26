/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //LENGTH OF LINKED LIST
        int length = 0;
        ListNode tracker = head;
        ListNode previous = head;
        while(tracker!=null){
            length++;
            tracker = tracker.next;
        }

        tracker = head;
        if(length == n){
            head = head.next;
            return head;
        }
        while(length!=n){
            previous = tracker;
            tracker = tracker.next;
            length-=1;
        }
        
        previous.next = previous.next.next;
        return head;



        
        

    }
}
