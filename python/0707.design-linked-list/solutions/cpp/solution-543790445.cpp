// leetcode.cn/problems/design-linked-list/  (707)
// submission 543790445  accepted 2024-07-03  runtime 38 ms  memory 22.9 MB

class MyLinkedList
{
private:
    struct ListNode
    {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    // 设置虚拟头结点，简化寻找目标结点的前一结点的过程
    ListNode *dummy;

public:
    int size;
    MyLinkedList()
    {
        dummy = new ListNode();
        size = 0;
    }

    int get(int index)
    {
        ListNode *p = dummy;
        if (index < 0 || index >= size)
            return -1;
        // 由于p初始在第一个实际结点的前面，故移动index次只能找到目标结点的前一个结点
        for (int i = 0; i <= index; i++)
            p = p->next;
        return p->val;
    }

    void addAtHead(int val)
    {
        addAtIndex(0, val);
    }

    void addAtTail(int val)
    {
        addAtIndex(size, val);
    }

    void addAtIndex(int index, int val)
    {
        if (index < 0 || index > size)
            return;
        ListNode *p = dummy;
        for (int i = 0; i < index; i++)
        {
            p = p->next;
        }
        p->next = new ListNode(val, p->next);
        size++;
    }

    void deleteAtIndex(int index)
    {
        if (index < 0 || index >= size)
            return;
        ListNode *p = dummy;
        for (int i = 0; i < index; i++)
        {
            p = p->next;
        }
        ListNode *temp = p->next;
        p->next = temp->next;
        delete (temp);
        size--;
    }
    void print()
    {
        ListNode *p = dummy;
        while (p != nullptr)
        {
            if (p != dummy)
            {
                std::cout << p->val << ", ";
            }
            p = p->next;
        }
        std::cout << std::endl;
    }
};


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
