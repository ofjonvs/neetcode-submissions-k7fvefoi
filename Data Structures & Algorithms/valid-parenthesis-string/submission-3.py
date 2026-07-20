class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOp = minOp = 0
        for c in s:
            match c:
                case '(':
                    maxOp += 1
                    minOp += 1
                case ')':
                    maxOp -= 1
                    minOp -= 1
                    if maxOp < 0:
                        return False
                case '*':
                    maxOp += 1
                    minOp -= 1
            minOp = max(minOp, 0)
        return not minOp