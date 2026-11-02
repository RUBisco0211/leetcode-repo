// leetcode.cn/problems/merge-two-sorted-lists/  (21)
// submission 412844623  accepted 2023-03-13  runtime 0 ms  memory 6 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    typedef struct ListNode LNode;
    LNode* L = (LNode*)malloc(sizeof(LNode));
    LNode* p = L;
    if(list1 == NULL)
    return list2;
    else if(list2 == NULL)
    return list1;
    else if(list1 == NULL && list2 == NULL)
    return NULL;
    while(list1 != NULL && list2 != NULL){
        if(list1->val <= list2->val){
            p->next = list1;
            list1 = list1->next;
        }
        else{
            p->next = list2;
            list2 = list2->next;
        }
        p = p->next;
    }
    p->next = list1==NULL?list2 : list1;
    return L->next;
}
