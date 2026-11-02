// leetcode.cn/problems/intersection-of-two-linked-lists-lcci/  (面试题 02.07)
// submission 544129646  accepted 2024-07-04  runtime 43 ms  memory 16.6 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        if (headA == nullptr || headB == nullptr)
            return nullptr;
        ListNode *pA = headA, *pB = headB;
        while (pA != pB)
        {
            if (pA == nullptr)
                pA = headB;
            else
                pA = pA->next;

            if (pB == nullptr)
                pB = headA;
            else
                pB = pB->next;
        }
        return pA;
    }
};
