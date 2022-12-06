class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(N^2) complexity, O(1) space

        # store a tuple containing the closest num and distance from target
        close = (-1,float(inf)) 
        
        nums = sorted(nums) # we need to process this in sorted order O(N log N)

        # O(N) complexity
        for i in range(len(nums)-2):
            # This will be our first number (we wont change it during this iteration)
            first = nums[i]

            # Two pointer approach, l should be the pointer right after the first pointer
            # and r should be initialized to be the pointer at the end of the array
            # O(N) complexity
            l, r = i + 1, len(nums) - 1
            while l < r:
                tempSum = first + nums[l] + nums[r]

                # Check if current sum closest to target
                if abs(target - tempSum) < close[1]:
                    close = (tempSum, abs(target - tempSum))

                # Holding the first element in the 3sum constant, how do we increment / decrement
                # the sum? We can either make the 2nd element larger to increase the sum, or 
                # we can make the 3rd element smaller to decrease the sum.

                # We cannot decrement the 2nd element to decrease the sum, because the 2nd element may
                # overlap with the first element, and we cannot increment the 3rd element because 
                # the iteration index may fall out of bounds.

                # The whole point with this two pointer approach is that given that the first element of
                # a 3Sum is constant, we want to simulate the other possible two numbers that would form a 
                # sum that is close to the target.
                if tempSum < target:
                    l += 1
                else:
                    r -= 1

        return close[0]