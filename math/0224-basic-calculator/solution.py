class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        def build(i):
            nonlocal n
            op = '+'
            acc = 0
            stack = []
            def apply(op, value: int):
                if op == '+':
                    stack.append(value)
                else:
                    stack.append(-value)
            
            while i < n:
                ch = s[i]
                if ch.isspace():
                    i += 1
                elif ch.isnumeric():
                    acc = acc * 10 + int(ch)
                    i += 1
                elif ch in ['+', '-']:
                    apply(op, acc)
                    op = ch
                    acc = 0
                    i += 1
                elif ch == ')':
                    apply(op, acc)
                    return i + 1, sum(stack)
                else:
                    i, value = build(i + 1)
                    apply(op, value)
            if acc:
                apply(op, acc)
            return i, sum(stack)
        return build(0)[1]

