class Solution:
    # TC --> O((max-min+1) * N), SC --> O(1) using linear search approach
    def possible(self, nums, day, m, k):
        n = len(nums)
        cnt = 0
        noOfB = 0
        for i in range(n):

            if nums[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        val = m * k
        if val > n:
            return -1
        mini = float("inf")
        maxi = float("-inf")
        for num in bloomDay:
            mini = min(mini, num)
            maxi = max(maxi, num)
        for i in range(mini, maxi + 1):
            if self.possible(bloomDay, i, m, k):
                return i
        return -1
    
    # TC --> O(log(max-min+1) * N), SC --> O(1) using binary search approach
    def possible(self, nums, day, m, k):
        n = len(nums)
        cnt = 0
        noOfB = 0
        for i in range(n):

            if nums[i] <= day:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        val = m * k
        if val > n:
            return -1
        mini = float("inf")
        maxi = float("-inf")
        for num in bloomDay:
            mini = min(mini, num)
            maxi = max(maxi, num)
        low = mini
        high = maxi
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(bloomDay, mid, m, k) == True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 
