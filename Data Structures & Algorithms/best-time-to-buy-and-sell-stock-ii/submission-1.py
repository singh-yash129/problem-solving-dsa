class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        # Start from the second day (index 1)
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's
            if prices[i] > prices[i - 1]:
                # "Capture" that small profit jump
                total_profit += prices[i] - prices[i - 1]
                
        return total_profit