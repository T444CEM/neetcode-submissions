class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                value = stack[(len(stack) - 2)] + stack[(len(stack) - 1)]
                stack.append(value)
            elif op == "D":
                value = stack[(len(stack) - 1)] * 2
                stack.append(value)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
            
        return sum(stack)