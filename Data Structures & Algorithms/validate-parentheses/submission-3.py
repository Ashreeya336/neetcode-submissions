class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack = []
        open_close = {')': '(', ']' : '[', '}': '{'}
        for i in s:
            if i == '(' or i =='[' or i =='{':
                stack.append(i)
            else: 
                if len(stack) == 0 or  open_close[i] != stack.pop(-1):
                    return False
        return len(stack) == 0