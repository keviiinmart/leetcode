#122.Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1
        totalP, maxP = 0,0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                print(prices[buy])
                print(prices[sell])
                totalP = totalP + prices[sell] - prices[buy]
                print(totalP)
                buy = sell
            else:
                buy = sell
            sell += 1
        return totalP

