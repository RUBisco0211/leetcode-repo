# leetcode.cn/problems/valid-parentheses/  (20)
# submission 752851894  accepted 2026-10-05  runtime 0 ms  memory 19 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            match ch:
                case '(' | '{' | '[':
                    stack.append(ch)
                case ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                case ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
