class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        fi = 0
        fiminus1 = 0
        profit = 0
        for i in range(1, len(prices)):
            fi = max((prices[i] - prices[i-1] + fiminus1), 0)
            profit = max(fi, profit)
            fiminus1 = fi
        return profit