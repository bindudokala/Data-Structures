class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # using Stack
        stack = []
        for op in operations:
            if op == 'C' and len(stack) > 0:
                stack.pop()
            elif op == 'D'and len(stack) > 0:
                stack.append(2 * stack[-1])
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)