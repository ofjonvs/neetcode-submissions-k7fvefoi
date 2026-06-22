class Twitter:

    def __init__(self):
        self.tweetIds = collections.defaultdict(list)
        self.time = 0
        self.followings = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append((tweetId, self.time))
        self.time -= 1
        len(self.tweetIds[userId]) > 10 and self.tweetIds[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for following in self.followings.get(userId, set())|{userId}:
            if not self.tweetIds[following]:
                continue
            lastTweet, time = self.tweetIds[following][-1]
            heapq.heappush_max(heap, (time, lastTweet, following, -1))
            if len(heap) > 10:
                heapq.heappop_max(heap)
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) != 10:
            _, tweetId, user, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if -idx < len(self.tweetIds[user]):
                lastTweet, time = self.tweetIds[user][idx-1]
                heapq.heappush(heap, (time, lastTweet, user, idx-1))
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerId in self.followings and self.followings[followerId].discard(followeeId)
