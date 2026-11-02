// leetcode.cn/problems/implement-queue-using-stacks/  (232)
// submission 544575229  accepted 2024-07-06  runtime 0 ms  memory 8.3 MB

#include <stack>

class MyQueue
{
private:
    std::stack<int> input_stack;
    std::stack<int> output_stack;

public:
    MyQueue()
    {
    }

    void push(int x)
    {
        input_stack.push(x);
    }

    int pop()
    {
        if (output_stack.empty())
        {
            while (!input_stack.empty())
            {
                int top = input_stack.top();
                output_stack.push(top);
                input_stack.pop();
            }
        }
        int top = output_stack.top();
        output_stack.pop();
        return top;
    }

    int peek()
    {
        if (output_stack.empty())
        {
            while (!input_stack.empty())
            {
                int top = input_stack.top();
                output_stack.push(top);
                input_stack.pop();
            }
        }
        return output_stack.top();
    }

    bool empty()
    {
        return input_stack.empty() && output_stack.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
