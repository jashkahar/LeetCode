class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            print(cur, "Curr")
            print(stack, "stack")
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur !=  "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)

                    