from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.timestamp=0
        self.userTweetsMap=defaultdict(list)
        self.followerMap=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp+=1
        self.userTweetsMap[userId].append((-self.timestamp,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        heap.extend(self.userTweetsMap[userId][-10:])
        for followeeId in self.followerMap[userId]:
            heap.extend(self.userTweetsMap[followeeId][-10:])

        heapq.heapify(heap)
        feed=[]
        print(heap)
        while heap and len(feed)<10:
            feed.append(heapq.heappop(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and followerId in self.followerMap and followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)