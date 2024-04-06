class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        c = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                continue
            # print(stack)
        
        # print(stack)
        res = ''
        
        for i in range(len(s)):
            if i in stack:
                continue
            else:
                res += s[i]
        return res
            