class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        meow = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in meow:
                if not stack or meow[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return not stack