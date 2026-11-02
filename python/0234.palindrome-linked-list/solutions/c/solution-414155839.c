// leetcode.cn/problems/palindrome-linked-list/  (234)
// submission 414155839  accepted 2023-03-16  runtime 156 ms  memory 40.4 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head){
    int temp[100000],len = 0;
    typedef struct ListNode LNode;
    LNode* p = head;
    while(p!= NULL){
        temp[len++] = p->val;
        p = p->next;
    }
    for(int left=0,right=len-1;left<right;left++,right--)
        if(temp[left]!=temp[right])
            return false;
    return true;
}
