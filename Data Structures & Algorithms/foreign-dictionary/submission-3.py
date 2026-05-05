class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        groups = [(words, 0)]
        while groups:
            newGroups = []
            for groupWords, currCharIdx in groups:
                currChar = None
                newGroup = []
                for i, word in enumerate(groupWords):
                    if currCharIdx >= len(word):
                        break
                    if (newChar:=word[currCharIdx]) != currChar:
                        adj.setdefault(currChar, []).append(newChar)
                        currChar = newChar
                        newGroups.append((newGroup, currCharIdx+1))
                        newGroup = [word]
                    else:
                        if len(word) < len(groupWords[i-1]):
                            return ''
                        newGroup.append(word)
                newGroup and newGroups.append((newGroup, currCharIdx+1))

            groups = newGroups
        adj.pop(None)
        
        seen = set()
        order = []
        for c in adj:
            path = set()
            def search(x):
                if x in path:
                    return False
                if x in seen:
                    return True
                seen.add(x)
                path.add(x)
                ret = True
                for neighbor in adj.get(x, []):
                    ret = search(neighbor) and ret
                order.append(x)
                path.remove(x)
                return ret
            if not search(c):
                return ''

        return ''.join(order[::-1]) + ''.join({c for w in words for c in w if c not in seen})
