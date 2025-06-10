import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.userFollows = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.count, tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res, maxHeap = [], []
        self.userFollows[userId].add(userId)
        for f in self.userFollows[userId]:
            if self.userTweets[f]:
                indx = len(self.userTweets[f]) - 1
                c, tId = self.userTweets[f][indx]
                maxHeap.append([c, tId, f, indx - 1])
        heapq.heapify(maxHeap)
        
        while maxHeap and len(res) < 10:
            c, tId, f, indx = heapq.heappop(maxHeap)
            res.append(tId)
            if indx >= 0:
                c, tId = self.userTweets[f][indx]
                heapq.heappush(maxHeap, [c, tId, f, indx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)



'''
💡 Main Idea
This design uses:

• A hashmap of lists to track each user's tweets.
    • Each tweet is stored with a global count (decreasing integer) to maintain order without needing timestamps.

• A hashmap of sets to track each user's follow relationships.

• A max-heap (priority queue) to efficiently fetch the top 10 most recent tweets from the user’s followees (including themselves).

• Tweets are pushed into the heap using their count as the priority, and additional parameters like tweet ID, current followee, 
and the index of next followee to track the next most recent tweet that comes in the user news feed.


⏳ Time : getNewsFeed - O(m log m)
🗂️ Space : getNewsFeed - O(m)
m = number of users userId follows (including themselves)
'''