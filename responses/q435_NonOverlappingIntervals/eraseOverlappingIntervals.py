class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(N log N) complexity, O(1) space
        # First we sort (because intervals are not guarenteed to be in order) 
        # By the order of intervals (start,end) so the conditional statement for checking
        # if they're overlapping would work for all elements
        intervals.sort()

        lastIntervalEnd = intervals[0][1]
        remove = 0

        # Then we simply do an O(N) loop where we compare the last interval to the current
        # interval to see if they're matching
        # 
        # 1) If they're matching, increment the count of remove
        # 2) If they're not matching, the current interval is now the previous interval
        #
        # This O(N) loop will give us the solution as long as the intervals are sorted properly 
        # (see the sorting comment above) 
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastIntervalEnd:
                # overlapping (increment remove, don't update lastInterval because this is a duplicate)
                remove += 1

                # this is an overlapping interval, so we update lastIntervalEnd to be the smaller
                # end of the two intervals end values (current interval's end, and lastIntervalEnd)
                # This update lets this code handle prioritize removing intervals with large ranges
                # over removing intervals with smaller ranges
                
                # See: case where intervals = [[1,2],[2,3],[3,5],[0,10]]
                # 10 would be the initial lastIntervalEnd, but then it would quickly be updated to 2 in
                # the first iteration, thus we only had to delete one interval [0,10] instead of the rest
                # of the intervals to accommodate the large interval 
                lastIntervalEnd = min(lastIntervalEnd, intervals[i][1])
            else:
                lastIntervalEnd = intervals[i][1] # update last interval end
            
        return remove