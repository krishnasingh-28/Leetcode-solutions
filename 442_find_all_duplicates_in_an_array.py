class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # TC --> O(N), SC --> O(1)
        res = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                res.append(index+1)
            nums[index] = - nums[index]
        return res