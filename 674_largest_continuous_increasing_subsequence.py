class Solution:
    #TC -->O(N), SC -->O(1)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i==0:
                c = 1
                res = 1
                continue
            if (nums[i] > nums[i-1]):
                c += 1
            else:
                c = 1
            res = max(c, res)
        return res