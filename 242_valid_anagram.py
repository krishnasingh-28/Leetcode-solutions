class Solution:
    # TC --> O(N log N), SC --> O(N)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)