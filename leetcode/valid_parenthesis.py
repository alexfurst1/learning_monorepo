class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs.values():        # opening bracket
                stack.append(ch)
            elif ch in pairs:               # closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False            # mismatch or premature close
                stack.pop()

        return not stack                    # True iff everything matched
