class Solution:
    # TC --> O(N), SC --> O(1)
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c in "aeiou":
                return True
        return False
