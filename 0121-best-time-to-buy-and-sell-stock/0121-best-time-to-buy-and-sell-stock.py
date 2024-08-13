class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
    # (Sliding-window problem)    
    
        # use two-pointer: left = buy, right = sell
        l, r = 0, 1
        # set max profit to 0 as default case
        maxP = 0
    
        # keep iterating through array while right pointer has not past the end of prices
        while r < len(prices):
            # check for profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # take the maximum of the current max profit vs profit we just calculated
                maxP = max(maxP, profit)
            
            # if it's NOT a profitable transaction, we update the left pointer
            else:
                # if the left price ISN'T less than the right price, then we shift it
                # all the way to the right since we found a new lowest price
                l = r
            # keep updating the right pointer until end of array    
            r += 1
        
        return maxP