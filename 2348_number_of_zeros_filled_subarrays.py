class Solution:
    # TC --> O(N), SC --> O(1)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 0
        total += count * (count + 1) // 2
        return total
