class Solution:
    # TC --> O(N), SC -->O(1)
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        prev = None
        for i in range(len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1
            max_count = max(max_count, count)
        return max_count