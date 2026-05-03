class StockSpanner:

    def __init__(self):
        # We will store pairs: [price, span]
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # 1. While the stack isn't empty AND the previous price <= current price
        while self.stack and self.stack[-1][0] <= price:
            # 2. Add the previous price's span to our current span
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        
        # 3. Push the current price and its calculated span onto the stack
        self.stack.append([price, span])
        
        return span