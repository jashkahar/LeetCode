class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for val in num:
            while k>0 and stack and stack[-1]>val:
                k-=1
                stack.pop()
            if not stack and val=='0':
                continue
            stack.append(val)

        res = ''.join(stack)
        if k>0:
            res = res[:len(res)-k]
        return res if res else '0'