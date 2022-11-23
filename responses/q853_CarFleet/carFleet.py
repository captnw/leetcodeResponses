class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(N log N) complexity (mainly because of sorting), O(N) space
        cars = [(pos,spd) for pos,spd in zip(position,speed)]
        cars.sort(reverse=True) # We want to iterate in reverse to consider the cars closest to the target first
        # If we simply iterate normally from the beginning, it would be difficult to consider the cars further down the road
        # Because a car at any point may slow down and match the speed of the slower car if they reach another car.

        fleet = [] # our stack
        for pos,spd in cars:
            fleet.append((target-pos)/spd) # append the current car's time to reach the end to the fleet stack

            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                # if the previous car's time to reach the end is less than the older car's time to reach the end
                # it means that the previous car is faster than the older car, and it will catch up to the older car
                # remove the previous car's time to reach the end simply by popping it - O(1) operation
                fleet.pop()

        return len(fleet) 
