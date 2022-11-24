class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # This is a minimization problem with two pointers and binary search
        # l would be initialized to 1 (smallest number of bananas koko can eat per hour)
        # r would be the max of the piles (because eating each pile would only take 1 hour, the fastest rate koko can eat per pile)
        #
        # Let N be length of piles, and max(N) be the maximum value in piles 
        # Complexity is O(N log (max(N))) (binary search is O(log N), while simulation is O(max(N))), space is O(1)

        l, r = 1, max(piles)
        answer = max(piles)

        # utilizing binary search, O(log N) outerloop
        while l <= r:
            mid = l + (r - l)//2 # aka the number of bananas koko will eat at most per hour for this iteration
            # Simulate koko eating bananas O(max N)
            numHour = 0
            for pile in piles:
                numHour += math.ceil(pile / mid)

            if numHour <= h:
                # Koko's banana eating rate is valid if she can eat all of the bananas in a timely manner
                r = mid - 1
                answer = min(answer, mid)
            else:
                l = mid + 1

        return answer