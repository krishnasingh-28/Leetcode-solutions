class Solution:
    def possibleStringCount(self, word: str) -> int:
        # TC --> O(N), SC --> O(1)
        n = len(word)
        res = 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                res += 1
        return res
