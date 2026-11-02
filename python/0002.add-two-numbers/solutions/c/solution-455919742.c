// leetcode.cn/problems/add-two-numbers/  (2)
// submission 455919742  accepted 2023-08-13  runtime 12 ms  memory 7.4 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* result = (struct ListNode*)malloc(sizeof(struct ListNode));
    result->next = NULL;
    
    if(!l1 || !l2)
        return NULL;

    //工作指针
    struct ListNode* p = l1;  
    struct ListNode* q = l2;
    struct ListNode* s = result;

    //表示进位
    int carry = 0;

    //任意一个链表没有遍历结束的情况下
    while(p && q){
        s->val = (p->val + q->val + carry) % 10;
        carry = (p->val + q->val + carry) / 10;
        
        p = p->next;
        q = q->next;

        if(p && q){
            s->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            s->next->next = NULL;
            s = s->next;
        }
    }
    
    //两个链表都遍历完毕，若进位为0，直接返回result；否则在结尾添加一新结点
    if(!p && !q){
        if(carry){
            s->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            s->next->next = NULL;
            s = s->next;
            s->val = carry;
        }
        return result;
    }
        

    //r指针指向还未遍历完毕的链表并连接到结果链表后
    struct ListNode* remain = p ? p : q;
    s->next = remain;

    //进位为0，直接返回
    if(carry == 0)
        return result;

    //进位为1，连接并遍历余下的链表并依次进位
    while(s->next && carry){

        carry = (s->next->val + 1) / 10;
        s->next->val = (s->next->val + 1) % 10;
        s = s->next;
        
    }
    if(carry){
        s->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        s->next->next = NULL;
        s = s->next;
        s->val = carry;
    }
    return result;
}
