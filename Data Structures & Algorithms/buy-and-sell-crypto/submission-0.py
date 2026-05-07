class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = [0]
        
        for i in range (len(prices)):
            for j in range (i + 1, len(prices)):
                if prices[i] < prices[j]:
                    result.append(prices[j] - prices[i])
        return max(result)
        