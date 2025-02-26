class Solution:
    # Brute Force Approach 
    # TC --> O(n^2), SC --> O(1)
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for left in range(len(s)):
            for right in range(left+1,len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right-left-1)
        return ans 
    
    # Optimal Approach 
    # TC --> O(n), SC --> O(1)
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        d = {}
        for i,x in enumerate(s):
            if x not in d:
                d[x] = i
            else:
                ans = max(ans, i-1-d[x])
        return ans