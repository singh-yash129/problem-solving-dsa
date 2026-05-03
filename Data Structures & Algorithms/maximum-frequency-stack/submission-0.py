class FreqStack:

    def __init__(self):
        # Maps value to its current frequency
        self.cnt = {}
        # Maps frequency to a stack of values with that frequency
        self.stacks = {}
        # Current highest frequency
        self.max_f = 0

    def push(self, val: int) -> None:
        # Update the frequency of val
        f = self.cnt.get(val, 0) + 1
        self.cnt[val] = f
        
        # Update max_f if this is a new peak frequency
        if f > self.max_f:
            self.max_f = f
            self.stacks[f] = []
        
        # Add the value to the stack corresponding to its current frequency
        self.stacks[f].append(val)

    def pop(self) -> int:
        # Get the element from the stack of the current max frequency
        res = self.stacks[self.max_f].pop()
        
        # Decrement the count of the popped element
        self.cnt[res] -= 1
        
        # If the stack for the max frequency is empty, move down to the next level
        if not self.stacks[self.max_f]:
            self.max_f -= 1
            
        return res