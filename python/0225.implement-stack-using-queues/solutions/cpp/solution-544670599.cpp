// leetcode.cn/problems/implement-stack-using-queues/  (225)
// submission 544670599  accepted 2024-07-07  runtime 0 ms  memory 8.1 MB

#include <queue>

class MyStack
{
private:
    std::queue<int> input_queue;
    std::queue<int> output_queue;

public:
    MyStack()
    {
    }

    void push(int x)
    {
        input2output();
        input_queue.push(x);
        output2input();
    }
    void input2output()
    {
        while (!input_queue.empty())
        {
            int front = input_queue.front();
            input_queue.pop();
            output_queue.push(front);
        }
    }
    void output2input()
    {
        while (!output_queue.empty())
        {
            int front = output_queue.front();
            output_queue.pop();
            input_queue.push(front);
        }
    }

    int pop()
    {
        int front = input_queue.front();
        input_queue.pop();
        return front;
    }

    int top()
    {
        return input_queue.front();
    }

    bool empty()
    {
        return input_queue.empty() && output_queue.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
