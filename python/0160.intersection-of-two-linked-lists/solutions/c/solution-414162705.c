// leetcode.cn/problems/intersection-of-two-linked-lists/  (160)
// submission 414162705  accepted 2023-03-16  runtime 32 ms  memory 13.9 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    typedef struct ListNode LNode;
    LNode* pa = headA;
    LNode* pb = headB;
    while(pa!=pb){
        pa = pa->next;
        pb = pb->next;
        if(pa == NULL && pb ==NULL)
            return NULL;
        if(pa == NULL)
            pa = headB;
        if(pb == NULL)
            pb = headA;
    }
    return pa;
}
