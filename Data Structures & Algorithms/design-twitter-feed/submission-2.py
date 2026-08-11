class Twitter:

    def __init__(self):
        self.Users=defaultdict(set)
        self.Posts=defaultdict(list)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count-=1
        self.Posts[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followees=self.Users[userId]|{userId}
        maxHeap=[]
        res=[]
        for f in followees:
            for p in self.Posts[f]:
                maxHeap.append(p)
        heapq.heapify(maxHeap)
        for i in range(10):
            if maxHeap:
                res.append(heapq.heappop(maxHeap)[1])
            else:
                break
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.Users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.Users[followerId].discard(followeeId)
