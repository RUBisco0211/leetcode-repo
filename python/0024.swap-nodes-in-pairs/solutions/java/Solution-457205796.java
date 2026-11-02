// leetcode.cn/problems/swap-nodes-in-pairs/  (24)
// submission 457205796  accepted 2023-08-17  runtime 0 ms  memory 39.1 MB

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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode( 0, head );
        ListNode p = dummy;
        while( p.next != null && p.next.next != null ) {
            ListNode first = p.next, second = p.next.next;
            first.next = second.next;
            second.next = first;
            p.next = second;
            p = first;
        }
        return dummy.next;
    }
}
