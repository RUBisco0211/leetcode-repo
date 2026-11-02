// leetcode.cn/problems/remove-duplicates-from-sorted-list/  (83)
// submission 412865966  accepted 2023-03-13  runtime 0 ms  memory 6.2 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    typedef struct ListNode LNode;
    LNode* p = head;
    if(head == NULL)
    return head;
    while(p->next!=NULL){
        if(p->val == p->next->val){
            p->next = p->next->next;
        }
        else{
            p = p->next;
        }
    }
    return head;
}
