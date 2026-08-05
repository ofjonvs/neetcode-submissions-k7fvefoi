class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def helper(l, r):
            while l < r:
                m = (l + r) // 2
                midVal = mountainArr.get(m)
                if midVal == target:
                    return m
                elif midVal < (rightVal:=mountainArr.get(m+1)):
                    if target > midVal:
                        l = m+1
                    else:
                        r = m-1
                else:
                    if midVal > (leftVal:=mountainArr.get(m-1)):
                        leftSearch = helper(l, m-1)
                        return helper(m+1, r) if leftSearch == -1 else leftSearch
                    if target > midVal:
                        r = m-1
                    else:
                        l = m+1
            return l if mountainArr.get(l) == target else -1
        return helper(0, mountainArr.length()-1)