class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(N log N) complexity, O(N) space
        # First we sort intervals (because they're not guarenteed to be sorted)
        intervals.sort() # O(N log N) bottleneck

        # We start by having result contain the first interval
        # Then we iterate from 1 to N-1 for a total of N-1 iterations
        result = [intervals[0]] 

        # This for loop is an O(N) operation
        for i in range(1, len(intervals)): 
            # result[-1] always points to the last interval
            if intervals[i][0] > result[-1][1]:
                # if interval start is outside of the last interval's end range
                # we can append the current interval without any merging
                result.append(intervals[i])
            else:
                # we have a merge situation, we update the last interval's end property
                # we don't have to worry about updating the last interval's start property
                # because we've sorted the intervals, and it's guarenteed that the current interval's
                # start property is always larger or greater than the last interval's start property
                result[-1][1] = max(result[-1][1], intervals[i][1])

        return result 