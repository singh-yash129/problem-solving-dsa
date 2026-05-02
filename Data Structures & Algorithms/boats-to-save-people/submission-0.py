class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1. Sort the people to use the greedy approach
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest and heaviest can share a boat
            if people[left] + people[right] <= limit:
                left += 1
            
           
            right -= 1
            boats += 1
            
        return boats