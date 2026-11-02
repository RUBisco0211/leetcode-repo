// leetcode.cn/problems/reverse-linked-list/  (206)
// submission 543800593  accepted 2024-07-03  runtime 4 ms  memory 11.5 MB

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
    ListNode *reverseList(ListNode *p)
    // 函数含义：接收原链表p的后一个结点，将后一个结点到尾结点全部反转之后，返回新链表的头部（即原链表的尾部）
    {
        // 链表为空
        if (p == nullptr)
            return nullptr;
        // 原链表尾部的next为nullptr，原尾部即为新链表头部
        if (p->next == nullptr)
            return p;
        ListNode *head = reverseList(p->next);
        // 后方结点全部反转之后，反转p和p的后一个结点，并返回新的头结点
        p->next->next = p;
        p->next = nullptr;
        return head;
    }
};
