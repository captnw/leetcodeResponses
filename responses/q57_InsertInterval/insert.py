class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # O(N) complexity, O(N) space

        result = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                # newInterval is outside the range of the current interval
                # meaning newInterval should exist as a seperate interval before the current one
                result.append(newInterval)
                return result + intervals[i:]
                
            elif interval[1] < newInterval[0]:
                # current interval is outside the range of newInterval
                # meaning interval should exist as a seperate interval before the new one
                result.append(interval)
            else:
                # merge current interval and newInterval and store in newInterval
                # merging the two intervals is fairly trivial
                newInterval = (min(interval[0], newInterval[0]), max(interval[1], newInterval[1]))

        # We always append newInterval once we get out of the loop
        result.append(newInterval)

        return result