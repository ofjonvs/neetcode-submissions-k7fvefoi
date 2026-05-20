class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordA = ord('a')
        groups = {}
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ordA] += 1
            groups.setdefault(tuple(cnt), []).append(s)
        return list(groups.values())