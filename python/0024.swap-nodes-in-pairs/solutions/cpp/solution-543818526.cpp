// leetcode.cn/problems/swap-nodes-in-pairs/  (24)
// submission 543818526  accepted 2024-07-03  runtime 6 ms  memory 9.2 MB

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
    // 递归解法
    ListNode *swapPairs(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }
        // 交换p与p后方的结点
        ListNode *new_head = head->next;
        // 原先的前一个结点指向后方交换好的链表的新头结点
        head->next = swapPairs(new_head->next);
        new_head->next = head;
        return new_head;
    }
};
