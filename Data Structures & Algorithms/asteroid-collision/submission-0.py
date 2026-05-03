class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
        
            if stack and stack[-1] > 0 and asteroids[i] < 0:
           
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop() 
                    i += 1
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop() # Stack asteroid explodes, check current against new stack top
                   
                else:
                    i += 1      # Current asteroid is smaller, it explodes
            else:
                # No collision possible: same direction or moving away from each other
                stack.append(asteroids[i])
                i += 1
                
        return stack