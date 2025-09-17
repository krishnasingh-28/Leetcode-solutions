class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # TC --> O(N), SC --> O(1)
        for c in s:
            if c in "aeiou":
                return True
        return False
