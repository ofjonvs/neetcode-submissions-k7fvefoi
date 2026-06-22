class Twitter:

    def __init__(self):
        self.tweetIds = collections.defaultdict(list)
        self.tweetIdTimes = {}
        self.time = 0
        self.followings = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append(tweetId)
        self.tweetIdTimes[tweetId] = self.time
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        return sorted((tweetId for following in self.followings.get(userId, set())|{userId} for tweetId in self.tweetIds[following]), key=lambda x: self.tweetIdTimes[x])[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerId in self.followings and self.followings[followerId].discard(followeeId)
