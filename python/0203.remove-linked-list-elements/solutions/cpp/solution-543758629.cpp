// leetcode.cn/problems/remove-linked-list-elements/  (203)
// submission 543758629  accepted 2024-07-03  runtime 11 ms  memory 18.6 MB

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
    // 递归做法
    ListNode *removeElements(ListNode *p, int val)
    {
        if (p == nullptr)
            return nullptr;
        // 需要先确定当前结点p的next指向何处
        p->next = removeElements(p->next, val);
        // 再确定要返回的是当前结点还是下一结点
        if (p->val == val)
            return p->next;
        return p;
    }
};
