class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(N) complexity, O(1) space
        # costNow is the minimum cost for climbing the most recent step, while costPrev is the 
        # minimum cost for climbing the previous step (before the most recent)

        # we can always index at 0 or 1 since the constraints specify the len(cost) is at least 2
        costNow, costPrev = cost[1], cost[0] 

        # We have already accounted for the first two elements, therefore we're starting at index i = 2
        # and iterating for the rest of the elements in cost

        for i in range(2,len(cost)):
            # The approach with the two variables allow us to cache the minimum cost for two paths at a time
            # For every iteration, we're trying to minimize the cost of the idea:
            # "If we MUST take this step at index i, what would be the minimum cost of doing so?"
            
            # We would then consult the two variables to see which the costs of which path (costNow, or costPrev)
            # are cheaper, we can consider both of them during the same iteration because it only takes 1 step
            # from the step with price costNow to get to the current step, and it takes 2 steps from the step
            # with price costPrev to get to the current step.

            # We can get the minimum cost (for the current step) by fetching the cost of the current step, and the 
            # mininum cost of the two paths. costNow's price would need to be cached and stored in costPrev, and then
            # we can now store our new minimum cost in costNow.

            #
            #                                                                      ___ Step C: price = cost[i] + min(costNow, costPrev)___
            #                                     ___ Step B: price = costNow ____|
            # _____ Step A: price = costPrev ____| 
            #
            # 1) Take 2 steps from Step A, and pay price cost[i] + costPrev
            # 2) Take 1 step from Step B, and pay price cost[i] + costNow

            temp = costNow
            costNow = cost[i] + min(costNow, costPrev)
            costPrev = temp

            # Since this is Python you can certainly use python variable assignment notation to avoid the use of a third variable
            # But I avoided it here because the use of a third variable indicates that I'm trying to "swap variables"
            # and it gives me a reminder of how I approached the code for this problem
            # Example of Pythonic notation for variable swapping:
            # costNow, costPrev = cost[i] + min(costNow, costPrev), costNow

        # We have to find the minimum cost between costNow and costPrev, because one can still get to the end
        # from the step with cost costPrev by climbing 2 steps at a time
        return min(costNow, costPrev)