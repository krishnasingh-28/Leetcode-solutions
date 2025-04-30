class Solution:
    # TC --> O(N), SC --> O(1)
    def countHomogenous(self, s: str) -> int:
        ans = 0
        current_streak = 0
        mod = 10**9 + 7
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                current_streak += 1
            else:
                current_streak = 1
            ans = (ans + current_streak) % mod
        return ans
