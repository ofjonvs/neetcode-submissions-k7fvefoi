class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = wcStack = 0
        for c in s:
            match c:
                case '(':
                    openStack += 1
                case ')':
                    if openStack > 0:
                        openStack -= 1
                    elif wcStack > 0:
                        wcStack -= 1
                    else:
                        return False
                case '*':
                    wcStack += 1
        
        openStack = wcStack = 0
        for c in reversed(s):
            match c:
                case ')':
                    openStack += 1
                case '(':
                    if openStack > 0:
                        openStack -= 1
                    elif wcStack > 0:
                        wcStack -= 1
                    else:
                        return False
                case '*':
                    wcStack += 1
        return True