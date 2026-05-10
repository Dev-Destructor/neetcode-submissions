class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if char == ')' and last != '(':
                    return False
                if char == '}' and last != '{':
                    return False
                if char == ']' and last != '[':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
