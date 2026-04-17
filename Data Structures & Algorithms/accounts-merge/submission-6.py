class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = [[] for _ in range(len(accounts))]
        rank = [0]*len(accounts)
        emailAccMap = {}

        def getRoot(i):
            if isinstance(parents[i], int):
                parents[i] = getRoot(parents[i])
                return parents[i]
            return i

        for i, (name, *emails) in enumerate(accounts):
            for email in set(emails):
                if email in emailAccMap:
                    curRoot = getRoot(i)
                    emailRoot = getRoot(emailAccMap[email])
                    if curRoot != emailRoot:
                        big, small = (curRoot, emailRoot) if rank[curRoot] > rank[emailRoot] else (emailRoot, curRoot)
                        parents[small] = big
                        rank[big] += 1
                else:
                    emailAccMap[email] = i
        for email, nameIdx in emailAccMap.items():
            parents[getRoot(nameIdx)].append(email)
        return [[accounts[i][0]]+sorted(emails) for i, emails in enumerate(parents) if isinstance(emails, list)]


                