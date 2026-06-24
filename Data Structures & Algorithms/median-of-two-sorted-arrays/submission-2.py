class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        totalLen = len(nums1) + len(nums2)
        l1, r1 = 0, len(nums1) - 1
        while True:
            m1 = (l1 + r1) // 2
            m2 = totalLen//2 - m1 - 2
            
            n1val = nums1[m1] if m1 >= 0 else float('-inf')
            n2val = nums2[m2] if m2 >= 0 else float('-inf')
            n1Rightval = nums1[m1+1] if m1 + 1 < len(nums1) else float('inf')
            n2Rightval = nums2[m2+1] if m2 + 1 < len(nums2) else float('inf')

            if n1val <= n2Rightval and n2val <= n1Rightval:
                return min(n1Rightval, n2Rightval) if totalLen % 2 else (max(n1val, n2val) + min(n1Rightval, n2Rightval)) / 2
            elif n1val > n2Rightval:
                r1 = m1 - 1
            else:
                l1 = m1 + 1