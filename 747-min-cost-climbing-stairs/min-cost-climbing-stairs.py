class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        for i in range(2,n,1):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[n-1], cost[n-2])
            

            