class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        visited = set()
        queue = deque([target])
        turns = 0
        while queue:
            for i in range(len(queue)):
                comb = queue.popleft()
                if comb == '0000':
                    return turns
                if comb in visited or comb in deadends:
                    continue
                visited.add(comb)
                for i in range(4):
                    d = int(comb[i])
                    for j in (-1, 1):
                        newComb = comb[:i] + str((d+j)%10) + comb[i+1:]
                        queue.append(newComb)
                    
            turns += 1

        return -1