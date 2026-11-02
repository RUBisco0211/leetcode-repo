# leetcode.cn/problems/decode-string/  (394)
# submission 752858581  accepted 2026-10-05  runtime 0 ms  memory 19.1 MB

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue

            # 开始解析前面的字符串

            # 需要重复的字母串
            exp = ""
            while stack[-1] != '[':
                exp = stack.pop() + exp

            # 弹出 '['
            stack.pop()

            # 重复次数
            repeat, base = 0, 1
            while stack and '0' <= stack[-1] <= '9':
                repeat += int(stack.pop()) * base
                base *= 10
            
            # 解析成结果之后入栈
            stack.append(exp * repeat)
        return "".join(stack)
