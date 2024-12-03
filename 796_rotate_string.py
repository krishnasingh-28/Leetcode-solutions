class Solution:
    # Brute Force Approach TC --> O(N^2), SC --> O(N)
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False


    #Optimal approach TC --> O(N) , SC --> O(N)
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s 
        return goal in doubled_s

        