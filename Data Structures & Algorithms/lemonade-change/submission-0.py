class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = dict.fromkeys([5, 10], 0)
        for bill in bills:
            match bill:
                case 10:
                    if not register[5]:
                        return False
                    register[10] += 1
                    register[5] -= 1
                case 20:
                    if not register[10]:
                        if register[5] < 3:
                            return False
                        register[5] -= 3
                    elif not register[5]:
                        return False
                    else:
                        register[5] -= 1
                        register[10] -= 1
                case 5:
                    register[5] += 1
        return True
