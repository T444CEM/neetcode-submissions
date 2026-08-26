class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 == 1 or s[0] == "]" or s[0] == ")" or s[0] == "}":
            return False

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue

            if char == ")" and (not stack or stack[-1] != "("):
                return False
            elif char == "]" and (not stack or stack[-1] != "["):
                return False
            elif char == "}" and (not stack or stack[-1] != "{"):
                return False
            else:
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False