class Twitter:

    def __init__(self):
        # Using a defaultdict saves us the trouble of checking whether a userId exists within a dictionary or not

        # order doesn't matter that much since postTweet loops through all of your tweets and all of the tweets
        # from people you follow (so sorting will be involved)
        self.posts = defaultdict(set) 
        
        # here we want to use a set so that we can insert and remove from the followed set in constant time
        self.followed = defaultdict(set)
        
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        # We cannot assume tweetId is correlated with time, so we'll manage the time
        # property ourselves, we'll be using a min heap
        self.posts[userId].add((self.time,tweetId))
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        # N log N operation with priority queue
        # We're using a min heap and then sorting the results by time
        # because we can always ensure that the heap will be at most 10 during iteration
        # by tossing out the smallest value in the heap 
        minHeap = list()
        result = list()

        # We can definitely sort the posts by id since they're guarenteed to be unique
        # So inserting into heap will work.
        self.followed[userId].add(userId) # getNewsFeed return the recent posts of the people we followed, and our own posts

        # O(N * M), N = num users, M = num max posts
        for user in self.followed[userId]:
            for post in self.posts[user]:
                heapq.heappush(minHeap, post)

                # If heap is larger than 10, discard the latest/smallest post
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        # O(N * M), pop everything from heap to convert into list
        for _ in range(len(minHeap)):
            result.append(heapq.heappop(minHeap))

        # Since there can only be at most 10 elements in result,
        # We can sort result without incurring a heavy cost, 
        # since complexity would be at most O(10 log 10)
        # We negate the time within the lambda to sort by descending time
        result.sort(key = lambda pair : -pair[0])

        # O(10), convert the pair of values into the twitter post id, do this for all elements in result
        result = [pair[1] for pair in result]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # O(1) insertion
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(1) deletion
        followerSet = self.followed[followerId]
        if followeeId in followerSet:
            # This if statements handles the edge case of the followeeId not existing in followerSet
            followerSet.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)