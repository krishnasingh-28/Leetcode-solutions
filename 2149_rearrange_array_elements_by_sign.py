class Solution:
    # TC --> O(N+N/2), SC --> O(N)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(n // 2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        return nums
    
    # TC --> O(N) using optimal approach, SC --> O(N)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = 0, 1
        ans = [0] * n
        for i in range(n):
            if nums[i] < 0:
                ans[neg] = nums[i]
                neg += 2
            else:
                ans[pos] = nums[i]
                pos += 2
        return ans