class Solution:
    # TC --> O(N), SC --> O(N)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        strset = set(nums)
        for i in range(1, n + 1):
            if i not in strset:
                res.append(i)
        return res
