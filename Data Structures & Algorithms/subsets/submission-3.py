class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        st = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(st.copy())
                return
            
            j = i
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

            st.append(nums[j])
            dfs(j+1)
            st.pop()

        dfs(0)
        return res