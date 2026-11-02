// leetcode.cn/problems/linked-list-cycle-ii/  (142)
// submission 456527127  accepted 2023-08-15  runtime 0 ms  memory 42.5 MB

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(true){
            if( fast == null || fast.next == null)
                return null;
            fast = fast.next.next;
            slow = slow.next;
            if( fast == slow )
                break;
        }
        fast = head;
        while(fast != slow){
            fast = fast.next;
            slow = slow.next;
        }
        return slow;
    }
}
