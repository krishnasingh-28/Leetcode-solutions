class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TC --> O(N), SC --> O(N)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)