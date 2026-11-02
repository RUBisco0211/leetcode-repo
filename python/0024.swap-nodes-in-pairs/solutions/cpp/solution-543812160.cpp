// leetcode.cn/problems/swap-nodes-in-pairs/  (24)
// submission 543812160  accepted 2024-07-03  runtime 0 ms  memory 9.2 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *dummy = new ListNode(0, head);

        ListNode *p = dummy;
        // 两两交换涉及的结点为需要交换的两个结点以及它们之前的结点p
        while (p->next != nullptr && p->next->next != nullptr)
        {
            ListNode *first = p->next, *second = first->next;
            p->next = second;
            first->next = second->next;
            second->next = first;
            p = first;
        }
        return dummy->next;
    }
};
