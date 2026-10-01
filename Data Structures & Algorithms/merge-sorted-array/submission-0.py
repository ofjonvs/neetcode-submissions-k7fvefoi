class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1, -1, -1):
            nums1[i], nums1[i+n] = nums1[i+n], nums1[i]
        
        i, j, k = n, 0, 0
        while i < m+n and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        for i in range(i, m+n):
            nums1[k] = nums1[i]
            k += 1
        for j in range(j, n):
            nums1[k] = nums2[j]
            k += 1