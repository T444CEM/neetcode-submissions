class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 == 1 or s[0] == "]" or s[0] == ")" or s[0] == "}":
            return False

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue

            if char == ")" and len(stack) == 0:
                return False
            elif char == "]" and len(stack) == 0:
                return False
            elif char == "}" and len(stack) == 0:
                return False

            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False