class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-2
        i = -1
        while l < r:
            m = (l+r)//2
            if x > arr[m]:
                l = m + 1
            else:
                r = m
        if l == len(arr)-1:
            return arr[-k:]
        elif l == 0:
            return arr[:k]

        l, r = (l, l) if x - arr[l] < arr[l+1] - x else (l+1, l+1)
        while r-l+1 != k:
            if r == len(arr)-1:
                return arr[-k:]
            if l == 0:
                return arr[:k]
            print(l, r)
            if x-arr[l-1] <= arr[r+1]-x:
                l -= 1
            else:
                r += 1
        return arr[l:r+1]

        