class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections
        beginWord not in wordList and wordList.append(beginWord)
        graph = collections.defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if sum(int(c1 != c2) for c1, c2 in zip(wordList[i], wordList[j])) == 1:
                    graph[wordList[i]].add(wordList[j])
                    graph[wordList[j]].add(wordList[i])
        visited = {beginWord}
        queue = deque([beginWord])
        pathLen = 1
        while queue:
            pathLen += 1
            for i in range(len(queue)):
                for word in graph[queue.popleft()]:
                    if word in visited:
                        continue
                    if word == endWord:
                        return pathLen
                    queue.append(word)
                    visited.add(word)
        return 0