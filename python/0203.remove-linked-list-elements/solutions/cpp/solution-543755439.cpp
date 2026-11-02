// leetcode.cn/problems/remove-linked-list-elements/  (203)
// submission 543755439  accepted 2024-07-03  runtime 11 ms  memory 18.1 MB

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
    ListNode *removeElements(ListNode *head, int val)
    {
        // 哨兵位（若要删除head结点，需要设置哨兵位保留头指针），确保哨兵位的值与val不相等
        ListNode *dummy = new ListNode(val - 1, head);
        ListNode *p = dummy;
        while (p->next != nullptr)
        {
            if (p->next->val == val)
                p->next = p->next->next; // 跳过该结点
            else
                p = p->next; // 否则直接后移
        }
        return dummy->next;
    }
};
