# Problem: Design Twitter
# Pattern: Heap + HashMap
# Time:
# postTweet -> O(1)
# follow -> O(1)
# unfollow -> O(1)
# getNewsFeed -> O(f log f), where f = number of followed users
# Space: O(n)

from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(min_heap, [time, tweetId, followeeId, index - 1])

        while min_heap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(min_heap, [time, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


if __name__ == "__main__":

    twitter = Twitter()

    twitter.postTweet(1, 10)
    twitter.postTweet(2, 20)

    print(twitter.getNewsFeed(1))  # [10]
    print(twitter.getNewsFeed(2))  # [20]

    twitter.follow(1, 2)

    print(twitter.getNewsFeed(1))  # [20, 10]
    print(twitter.getNewsFeed(2))  # [20]

    twitter.unfollow(1, 2)

    print(twitter.getNewsFeed(1))  # [10]