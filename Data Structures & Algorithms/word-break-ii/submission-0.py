class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        out = []
        def recurse(i, curWord, curSentence):
            if i == len(s)-1:
                curWord += s[i]
                if curWord in wordDict:
                    out.append((curSentence + ' ' + curWord).strip())
                return
                
            curWord += s[i]
            if curWord in wordDict:
                recurse(i+1, '', curSentence+' '+curWord)
            recurse(i+1, curWord, curSentence)
        recurse(0, '', '')
        print(out)
        return out
