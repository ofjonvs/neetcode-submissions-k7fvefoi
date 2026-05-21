class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s))+','+s for s in strs)

    def decode(self, s: str) -> List[str]:
        curLen = ''
        decodedList = []
        curIdx = 0
        i = 0
        while i < len(s):
            if s[i] != ',':
                curLen += s[i]
                i += 1
            else:
                curLen = int(curLen)
                decodedList.append(s[i+1:i+curLen+1])
                i = i + curLen+1
                curLen = ''
        return decodedList
