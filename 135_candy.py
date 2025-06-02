class Solution:
    # Brute Force Approach
    # TC --> O(3N), SC --> O(2N)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        left = [1]*n
        right = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
        ans = 0
        for i in range(n):
            ans += max(left[i],right[i])
        return ans
    
    # Better Approach
    # TC --> O(2N), SC --> O(N)
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        cur = 1
        right = 1
        sum_candies = max(1, left[n - 1])
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cur = right + 1
            else:
                cur = 1
            right = cur
            sum_candies += max(left[i], cur)
        return sum_candies
