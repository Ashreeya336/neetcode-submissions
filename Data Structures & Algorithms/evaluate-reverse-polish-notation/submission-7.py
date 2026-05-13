class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '*':
                stack.append(stack.pop(-1) * stack.pop(-1))
            elif i == '+':
                stack.append(stack.pop(-1) + stack.pop(-1))
            elif i == '-':
                top = stack.pop(-1)
                stack.append(stack.pop(-1) - top)
            elif i == '/':
                top = stack.pop(-1)
                stack.append(int(stack.pop(-1) / top))
            else: 
                stack.append(int(i))
            print(stack)
        return stack[-1]
