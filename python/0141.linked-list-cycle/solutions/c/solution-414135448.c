// leetcode.cn/problems/linked-list-cycle/  (141)
// submission 414135448  accepted 2023-03-16  runtime 8 ms  memory 7.8 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    typedef struct ListNode LNode;
    if(head == NULL||head->next == NULL)
    return false;
    LNode* slow = head;
    LNode* fast = head->next;
    while(slow!=fast){
        if(fast == NULL||fast->next == NULL)
        return false;
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}
