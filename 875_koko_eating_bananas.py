class Solution:
    # Brute Force Approach using linear search
    # TC --> O(m*n), SC --> O(1), m = max(piles)
    def totalhours(self, piles, h):
        totalhours = 0
        for i in range(len(piles)):
            totalhours += math.ceil(piles[i] / h)
        return totalhours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        for i in range(1, maxi + 1):
            reqTime = self.totalhours(piles, i)
            if reqTime <= h:
                return i
        return maxi
    
    # Optimal Approach using binary search
    # TC --> O(n*log(m)), SC --> O(1), m = max(piles)
    def totalhours(self, piles, h):
        totalhours = 0
        for i in range(len(piles)):
            totalhours += math.ceil(piles[i] / h)
        return totalhours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if self.totalhours(piles, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low